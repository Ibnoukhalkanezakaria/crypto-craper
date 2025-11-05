"""
Alert notification system.
Sends alerts via Telegram, Discord, and Email.
"""
import aiohttp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict
from loguru import logger
from config.settings import settings
from models.database import Alert
from datetime import datetime


class AlertNotifier:
    """
    Multi-channel alert notification system.
    """
    
    def __init__(self):
        self.telegram_enabled = (
            settings.enable_telegram_alerts and 
            settings.telegram_bot_token
        )
        self.discord_enabled = (
            settings.enable_discord_alerts and 
            settings.discord_webhook_url
        )
        self.email_enabled = (
            settings.enable_email_alerts and 
            settings.smtp_host
        )
    
    async def send_telegram(self, message: str) -> bool:
        """
        Send alert via Telegram.
        
        Args:
            message: Message to send
            
        Returns:
            True if successful
        """
        if not self.telegram_enabled:
            return False
        
        try:
            url = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
            params = {
                "chat_id": settings.telegram_chat_id,
                "text": message,
                "parse_mode": "Markdown"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=params) as response:
                    if response.status == 200:
                        logger.info("Telegram alert sent successfully")
                        return True
                    else:
                        logger.error(f"Telegram error: {response.status}")
                        return False
                        
        except Exception as e:
            logger.error(f"Error sending Telegram alert: {e}")
            return False
    
    async def send_discord(self, message: str, embed: Dict = None) -> bool:
        """
        Send alert via Discord webhook.
        
        Args:
            message: Message to send
            embed: Optional embed data
            
        Returns:
            True if successful
        """
        if not self.discord_enabled:
            return False
        
        try:
            payload = {"content": message}
            
            if embed:
                payload["embeds"] = [embed]
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    settings.discord_webhook_url,
                    json=payload
                ) as response:
                    if response.status == 204:
                        logger.info("Discord alert sent successfully")
                        return True
                    else:
                        logger.error(f"Discord error: {response.status}")
                        return False
                        
        except Exception as e:
            logger.error(f"Error sending Discord alert: {e}")
            return False
    
    def send_email(self, subject: str, body: str) -> bool:
        """
        Send alert via email.
        
        Args:
            subject: Email subject
            body: Email body
            
        Returns:
            True if successful
        """
        if not self.email_enabled:
            return False
        
        try:
            msg = MIMEMultipart()
            msg["From"] = settings.email_from
            msg["To"] = settings.email_to
            msg["Subject"] = subject
            
            msg.attach(MIMEText(body, "html"))
            
            server = smtplib.SMTP(settings.smtp_host, settings.smtp_port)
            server.starttls()
            server.login(settings.smtp_username, settings.smtp_password)
            server.send_message(msg)
            server.quit()
            
            logger.info("Email alert sent successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error sending email alert: {e}")
            return False
    
    def format_alert_message(self, alert: Alert) -> str:
        """
        Format alert as text message.
        
        Args:
            alert: Alert object
            
        Returns:
            Formatted message
        """
        severity_emoji = {
            "low": "ℹ️",
            "medium": "⚠️",
            "high": "🔴",
            "critical": "🚨"
        }
        
        emoji = severity_emoji.get(alert.severity, "📢")
        
        message = f"""
{emoji} **{alert.title}**

{alert.message}

Severity: {alert.severity.upper()}
Time: {alert.created_at.strftime('%Y-%m-%d %H:%M UTC')}
        """
        
        return message.strip()
    
    def format_discord_embed(self, alert: Alert) -> Dict:
        """
        Format alert as Discord embed.
        
        Args:
            alert: Alert object
            
        Returns:
            Discord embed dictionary
        """
        color_map = {
            "low": 0x3498db,      # Blue
            "medium": 0xf39c12,   # Orange
            "high": 0xe74c3c,     # Red
            "critical": 0x992d22  # Dark red
        }
        
        embed = {
            "title": alert.title,
            "description": alert.message,
            "color": color_map.get(alert.severity, 0x95a5a6),
            "fields": [
                {
                    "name": "Severity",
                    "value": alert.severity.upper(),
                    "inline": True
                },
                {
                    "name": "Alert Type",
                    "value": alert.alert_type,
                    "inline": True
                }
            ],
            "timestamp": alert.created_at.isoformat(),
            "footer": {
                "text": "Crypto Research AI Agent"
            }
        }
        
        return embed
    
    async def send_alert(self, alert: Alert):
        """
        Send alert through all enabled channels.
        
        Args:
            alert: Alert object to send
        """
        message = self.format_alert_message(alert)
        
        # Send via Telegram
        if self.telegram_enabled:
            await self.send_telegram(message)
        
        # Send via Discord
        if self.discord_enabled:
            embed = self.format_discord_embed(alert)
            await self.send_discord("", embed=embed)
        
        # Send via Email
        if self.email_enabled:
            self.send_email(
                subject=f"[Crypto Agent] {alert.title}",
                body=f"<html><body><pre>{message}</pre></body></html>"
            )
    
    async def send_phase_transition_alert(
        self, 
        symbol: str, 
        old_phase: str, 
        new_phase: str, 
        confidence: float
    ):
        """
        Send alert for phase transition.
        
        Args:
            symbol: Cryptocurrency symbol
            old_phase: Previous phase
            new_phase: New phase
            confidence: Detection confidence
        """
        message = f"""
🔄 **Phase Transition Detected: {symbol}**

{symbol} has transitioned from **{old_phase}** to **{new_phase}**

Confidence: {confidence:.1%}

This may indicate a change in market dynamics. Review your position.
        """
        
        if self.telegram_enabled:
            await self.send_telegram(message.strip())
        
        if self.discord_enabled:
            embed = {
                "title": f"Phase Transition: {symbol}",
                "description": f"{old_phase} → {new_phase}",
                "color": 0x3498db,
                "fields": [
                    {"name": "Confidence", "value": f"{confidence:.1%}", "inline": True},
                    {"name": "Symbol", "value": symbol, "inline": True}
                ],
                "timestamp": datetime.utcnow().isoformat()
            }
            await self.send_discord("", embed=embed)
    
    async def send_high_score_alert(
        self,
        symbol: str,
        score: float,
        phase: str,
        recommendation: str
    ):
        """
        Send alert for high opportunity score.
        
        Args:
            symbol: Cryptocurrency symbol
            score: Opportunity score
            phase: Market phase
            recommendation: Investment recommendation
        """
        message = f"""
⭐ **High Opportunity Detected: {symbol}**

Opportunity Score: **{score:.1f}/100**
Market Phase: **{phase}**
Recommendation: **{recommendation}**

This coin shows strong potential based on multi-factor analysis.
        """
        
        if self.telegram_enabled:
            await self.send_telegram(message.strip())
        
        if self.discord_enabled:
            embed = {
                "title": f"High Opportunity: {symbol}",
                "description": f"Score: {score:.1f}/100",
                "color": 0x2ecc71,  # Green
                "fields": [
                    {"name": "Phase", "value": phase, "inline": True},
                    {"name": "Recommendation", "value": recommendation, "inline": True}
                ],
                "timestamp": datetime.utcnow().isoformat()
            }
            await self.send_discord("", embed=embed)


# Example usage
if __name__ == "__main__":
    import asyncio
    
    async def test():
        notifier = AlertNotifier()
        
        await notifier.send_phase_transition_alert(
            symbol="BTC",
            old_phase="accumulation",
            new_phase="expansion",
            confidence=0.85
        )
        
        await notifier.send_high_score_alert(
            symbol="ETH",
            score=87.5,
            phase="accumulation",
            recommendation="BUY"
        )
    
    asyncio.run(test())
