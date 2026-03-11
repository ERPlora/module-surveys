"""
AI context for the Surveys module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Surveys

### Models

**Survey** — A survey with multiple questions.
- `title`, `description`
- `is_active`
- `start_date`, `end_date` (DateField, optional): Survey window
- `response_count` (PositiveIntegerField, cached): Total responses received

**SurveyQuestion** — A question within a survey.
- `survey` FK → Survey (related_name='questions')
- `text` (max 500 chars): The question text
- `question_type` (CharField, default 'text'): Type of answer expected (e.g., 'text', 'multiple_choice', 'rating', 'yes_no')
- `is_required` (bool, default True)
- `order` (PositiveIntegerField, default 0): Display order

### Key Flows

1. **Create survey**: Create Survey with title and optional date window → add SurveyQuestions in order
2. **Activate**: Set `is_active=True` and configure `start_date`/`end_date` if needed
3. **Collect responses**: (handled externally — no SurveyResponse model in this module) increment `response_count` manually
4. **Close survey**: Set `is_active=False` or let `end_date` pass

### Notes
- This is a minimal survey framework. The models define survey structure (questions) but do not include a SurveyResponse model for storing answers.
- For richer feedback collection with scoring and customer linking, see the Feedback module.
- `question_type` values are freeform strings — common values: 'text', 'multiple_choice', 'rating', 'yes_no', 'scale'
"""
