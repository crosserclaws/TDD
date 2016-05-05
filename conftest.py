#!/usr/bin/env python3

import pytest
import hello

@pytest.fixture
def app():
  return hello.app

@pytest.fixture
def test_client(app):
  app.testing = True
  client = app.test_client()
  return client