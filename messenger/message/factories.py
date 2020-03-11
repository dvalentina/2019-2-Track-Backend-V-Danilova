import factory
from message.models import Message

class SequenceMessagesFactory(factory.Factory):
    class Meta:
        model = Message

    user_id = 1
    chat_id = 0
    content = factory.Sequence(lambda n: 'Test Message N{0}'.format(n))
