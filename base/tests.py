from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import User, Topic, Room, Message
from .forms import MyUserCreationForm, RoomForm, UserForm


class ModelsTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username='testuser', email='test@gmail.com', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.check_password('testpassword'))

    def test_topic_creation(self):
        topic = Topic.objects.create(name='Test Topic')
        self.assertEqual(topic.name, 'Test Topic')

    def test_room_creation(self):
        user = User.objects.create_user(
            username='hostuser', email='host@gmail.com', password='hostpassword')
        topic = Topic.objects.create(name='Test Topic')
        room = Room.objects.create(host=user, topic=topic, name='Test Room')
        self.assertEqual(room.host, user)
        self.assertEqual(room.topic, topic)
        self.assertEqual(room.name, 'Test Room')

    def test_message_creation(self):
        user = User.objects.create_user(
            username='messageuser', email='message@gmail.com', password='messagepassword')
        topic = Topic.objects.create(name='Test Topic')
        room = Room.objects.create(host=user, topic=topic, name='Test Room')
        message = Message.objects.create(
            user=user, room=room, body='Test message')
        self.assertEqual(message.user, user)
        self.assertEqual(message.room, room)
        self.assertEqual(message.body, 'Test message')


class FormsTestCase(TestCase):
    def test_user_creation_form(self):
        form_data = {'name': 'Test User', 'username': 'testuser', 'email': 'test@gmail.com',
                     'password1': 'testpassword', 'password2': 'testpassword'}
        form = MyUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_room_form(self):
        user = User.objects.create_user(
            username='hostuser', email='host@gmail.com', password='hostpassword')
        topic = Topic.objects.create(name='Test Topic')
        form_data = {'topic': topic.id, 'name': 'Test Room'}
        form = RoomForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_form(self):
        user = User.objects.create_user(
            username='testuser', email='test@gmail.com', password='testpassword')
        form_data = {'avatar': 'test.jpg', 'name': 'Test User',
                     'username': 'testuser', 'email': 'test@gmail.com'}
        form = UserForm(instance=user, data=form_data)
        self.assertTrue(form.is_valid())
