from django.test import TestCase
from django.core import mail

# Create your tests here.

class SendEmail(TestCase):
    """
    This test to test the send of email
    """
    def test_send_email(self):
            """
            We test if a email is send
            """
            # Send message.
            mail.send_mail(
                'Demande de tarif',
                'Demande d\'échange de séance',
                'jacob@orange.fr', ['to@example.com'],
                fail_silently=False,
            )
            # time.sleep(2)
            # Test that one message has been sent.
            self.assertEqual(len(mail.outbox), 1)

            # Verify that the subject of the first message is correct.
            self.assertEqual(
                mail.outbox[0].subject,
                'Demande de tarif') 