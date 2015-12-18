import unittest

class Serializer(object):
    pass

class MessageSerializer(Serializer):
    sender = CharField(min_length=10, max_length=12)
    recipient = CharField()
    message = CharField()
    opt_jp = BooleanField(required=False)

    def validate_recipient(self, data):
        if data.startswith('81'):
            raise ValidationError('Not allowed to JP')
        return data

class TestMessageSerializer(unittest.TestCase):
    def test_send_sms_ok(self):
        data = {
            'sender': '71909191991',
            'recipient': '601818199810',
            'message': 'test',
        }

        serializer = MessageSerializer(data=data)
        assert serializer.is_valid() == True, serializer.is_valid()

    def test_send_sms_missing_recipient(self):
        data = {
            'sender': '71909191991',
            'recipient': '601818199810',
            'message': 'test',
        }

        serializer = MessageSerializer(data=data)
        assert serializer.is_valid() == False, serializer.is_valid()
        assert 'recipient' in serializer.errors, serializer.errors
        assert serializer.errors['recipient'] == ['is required']

    def test_opt_jp(self):
        data = {
            'sender': '71909191991',
            'recipient': '601818199810',
            'message': 'test',
            'opt_jp': 'true',
        }

        serializer = MessageSerializer(data=data)
        assert serializer.is_valid() is True, serializer.is_valid()
        assert serializer.validated_data['opt_jp'] is True, serializer.validated_data

if __name__ == '__main__':
    unittest.main()
