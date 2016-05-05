#!/usr/bin/env python3

import pytest

MOCK_ENCODING = 'mock-encoding'

class MockEncodingResponse:
  def __init__(self):
    self.headers = {'Content-Encoding': MOCK_ENCODING}

def _mock_get(url):
  assert url == 'https://news.ycombinator.com'
  return MockEncodingResponse()

@pytest.fixture
def mock_encoding_request(monkeypatch):
  monkeypatch.setattr('requests.get', _mock_get)

def test_encoding(test_client, mock_encoding_request):
  """
  GIVEN: A flask hellp app
         A mock request handler
  WHEN: I GET the /encoding route
  THEN: The response should be the expected Content-Encoding
  """
  resp = test_client.get('/encoding')
  assert resp.data.decode('utf-8') == MOCK_ENCODING
