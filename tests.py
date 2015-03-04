import unittest
from app import app
from config import MY_NR


class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_new_post(self):
        response = self.app.post('/new', data={'From': MY_NR})
        expected = (b'<?xml version="1.0" encoding="UTF-8"?>'
                    b'<Response>'
                    b'<Say>Hi!</Say>'
                    b'<Gather action="/handle-key" method="POST" numDigits="1">'
                    b'<Say>To record a post, press 1.</Say>'
                    b'</Gather>'
                    b'</Response>')
        self.assertEqual(expected, response.data)

    def test_handle_key(self):
        response = self.app.post('/handle-key', data={'Digits': '1'})
        expected = (b'<?xml version="1.0" encoding="UTF-8"?>'
                    b'<Response>'
                    b'<Say>Record your post after the tone.</Say>'
                    b'<Record action="/handle-recording" maxLength="30" />'
                    b'</Response>')
        self.assertEqual(expected, response.data)

    def test_handle_recording(self):
        response = self.app.post('/handle-recording', data={'RecordingUrl': 'something-random'})
        expected = (b'<?xml version="1.0" encoding="UTF-8"?>'
                    b'<Response><Say>Your post is now live! Goodbye</Say>'
                    b'</Response>')
        self.assertEqual(expected, response.data)

if __name__ == '__main__':
    unittest.main()