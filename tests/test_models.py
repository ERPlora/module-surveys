"""Tests for surveys models."""
import pytest
from django.utils import timezone

from surveys.models import Survey


@pytest.mark.django_db
class TestSurvey:
    """Survey model tests."""

    def test_create(self, survey):
        """Test Survey creation."""
        assert survey.pk is not None
        assert survey.is_deleted is False

    def test_str(self, survey):
        """Test string representation."""
        assert str(survey) is not None
        assert len(str(survey)) > 0

    def test_soft_delete(self, survey):
        """Test soft delete."""
        pk = survey.pk
        survey.is_deleted = True
        survey.deleted_at = timezone.now()
        survey.save()
        assert not Survey.objects.filter(pk=pk).exists()
        assert Survey.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, survey):
        """Test default queryset excludes deleted."""
        survey.is_deleted = True
        survey.deleted_at = timezone.now()
        survey.save()
        assert Survey.objects.filter(hub_id=hub_id).count() == 0

    def test_toggle_active(self, survey):
        """Test toggling is_active."""
        original = survey.is_active
        survey.is_active = not original
        survey.save()
        survey.refresh_from_db()
        assert survey.is_active != original


