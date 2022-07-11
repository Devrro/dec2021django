from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import os
from core.enums.template_enums import TemplateEnum
from core.services.jwt_service import JwtService


class EmailService:
    @staticmethod
    def _send_mail(to: str, tmpl_name: str, context: dict, subject='') -> None:
        template = get_template(tmpl_name)
        html_content = template.render(context)
        mail = EmailMultiAlternatives('Register', from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        mail.attach_alternative(html_content, r'text/html')
        mail.send()

    @classmethod
    def register_email(cls, user):
        token = JwtService.create_token(user)
        url = f'{os.environ.get("FRONTEND_URL")}/activate/{token}'
        cls._send_mail(user.mail, TemplateEnum.REGISTER.value, {'name': user.profile.name, 'link': url})

    @classmethod
    def reset_password(cls, user):
        token = JwtService.create_reset_token(user)
        url = f'{os.environ.get("FRONTEND_URL")}/activate/{token}'
        cls._send_mail(user.mail, TemplateEnum.RESET.value, {'name': user.profile.name, 'link': url})
