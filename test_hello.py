#!/usr/bin/env python3

import pytest

def test_hello(test_client):
  """
  GIVEN: A flask hellp app
  WHEN: I GET the hello/ route
  THEN: The response should be "Hello World!"
  """
  resp = test_client.get('/hello')
  assert resp.data.decode('utf-8') == 'Hello World!'
