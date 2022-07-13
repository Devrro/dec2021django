import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.enums.template_enums import TemplateEnum
from core.services.jwt_service import ActivateToken, JwtService, ResetPasswordToken


class EmailService:
    @staticmethod
    def _send_mail(to: str, tmpl_name: str, context: dict, subject='', title='') -> None:
        template = get_template(tmpl_name)
        html_content = template.render(context)
        mail = EmailMultiAlternatives(title, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        mail.attach_alternative(html_content, r'text/html')
        mail.send()

    @classmethod
    def register_email(cls, user):
        token = JwtService.create_token(user, ActivateToken)
        url = f'{os.environ.get("FRONTEND_URL")}/auth/activate/{token}'
        cls._send_mail(user.email, TemplateEnum.REGISTER.value, {'name': user.profile.name, 'link': url}, title='Register')

    @classmethod
    def reset_password(cls, user):
        token = JwtService.create_token(user,ResetPasswordToken)
        url = f'{os.environ.get("FRONTEND_URL")}/auth/reset/{token}'
        cls._send_mail(user.email, TemplateEnum.RESET.value, {'name': user.profile.name, 'link': url}, title='Reset password')
