"""
Tests for discourse_thread.py
"""
import pytest

# Basic smoke tests - does everything hang together?


def test_imports():
    from poller.discourse_thread import DiscourseThread

    test_poll = DiscourseThread("984627")
    assert test_poll.all_entrants[0] == "TwoCarrotSnowman"
