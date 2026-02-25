# Surveys Module

Advanced surveys, questionnaires and response analytics.

## Features

- Create surveys with title, description, and active date range
- Define questions with configurable type (text, multiple choice, etc.), required flag, and sort order
- Track response counts per survey
- Activate or deactivate surveys with start and end dates
- Dashboard with survey performance and response analytics

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Surveys > Settings**

## Usage

Access via: **Menu > Surveys**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/surveys/dashboard/` | Survey overview and response analytics |
| Surveys | `/m/surveys/surveys/` | Create and manage surveys and their questions |
| Responses | `/m/surveys/responses/` | View and analyze survey responses |
| Settings | `/m/surveys/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `Survey` | Survey with title, description, active status, start/end dates, and response count |
| `SurveyQuestion` | Question belonging to a survey with text, question type, required flag, and display order |

## Permissions

| Permission | Description |
|------------|-------------|
| `surveys.view_survey` | View surveys |
| `surveys.add_survey` | Create new surveys |
| `surveys.change_survey` | Edit existing surveys |
| `surveys.delete_survey` | Delete surveys |
| `surveys.view_responses` | View survey responses |
| `surveys.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
