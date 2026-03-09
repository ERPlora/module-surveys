# Surveys

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `surveys` |
| **Version** | `1.0.0` |
| **Icon** | `clipboard-outline` |
| **Dependencies** | None |

## Models

### `Survey`

Survey(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, title, description, is_active, start_date, end_date, response_count)

| Field | Type | Details |
|-------|------|---------|
| `title` | CharField | max_length=255 |
| `description` | TextField | optional |
| `is_active` | BooleanField |  |
| `start_date` | DateField | optional |
| `end_date` | DateField | optional |
| `response_count` | PositiveIntegerField |  |

### `SurveyQuestion`

SurveyQuestion(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, survey, text, question_type, is_required, order)

| Field | Type | Details |
|-------|------|---------|
| `survey` | ForeignKey | → `surveys.Survey`, on_delete=CASCADE |
| `text` | CharField | max_length=500 |
| `question_type` | CharField | max_length=20 |
| `is_required` | BooleanField |  |
| `order` | PositiveIntegerField |  |

## Cross-Module Relationships

| From | Field | To | on_delete | Nullable |
|------|-------|----|-----------|----------|
| `SurveyQuestion` | `survey` | `surveys.Survey` | CASCADE | No |

## URL Endpoints

Base path: `/m/surveys/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `responses/` | `responses` | GET |
| `surveys/` | `surveys_list` | GET |
| `surveys/add/` | `survey_add` | GET/POST |
| `surveys/<uuid:pk>/edit/` | `survey_edit` | GET |
| `surveys/<uuid:pk>/delete/` | `survey_delete` | GET/POST |
| `surveys/<uuid:pk>/toggle/` | `survey_toggle_status` | GET |
| `surveys/bulk/` | `surveys_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `surveys.view_survey` | View Survey |
| `surveys.add_survey` | Add Survey |
| `surveys.change_survey` | Change Survey |
| `surveys.delete_survey` | Delete Survey |
| `surveys.view_responses` | View Responses |
| `surveys.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_survey`, `change_survey`, `view_responses`, `view_survey`
- **employee**: `add_survey`, `view_responses`, `view_survey`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Surveys | `clipboard-outline` | `surveys` | No |
| Responses | `chatbox-ellipses-outline` | `responses` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_surveys`

List surveys.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `is_active` | boolean | No |  |

### `create_survey`

Create a survey with questions.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes |  |
| `description` | string | No |  |
| `start_date` | string | No |  |
| `end_date` | string | No |  |
| `questions` | array | No |  |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  icons/
    icon.svg
  surveys/
    css/
    js/
templates/
  surveys/
    pages/
      dashboard.html
      index.html
      responses.html
      settings.html
      survey_add.html
      survey_edit.html
      surveys.html
    partials/
      dashboard_content.html
      panel_survey_add.html
      panel_survey_edit.html
      responses_content.html
      settings_content.html
      survey_add_content.html
      survey_edit_content.html
      surveys_content.html
      surveys_list.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
