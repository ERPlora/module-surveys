"""AI tools for the Surveys module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListSurveys(AssistantTool):
    name = "list_surveys"
    description = "List surveys."
    module_id = "surveys"
    required_permission = "surveys.view_survey"
    parameters = {"type": "object", "properties": {"is_active": {"type": "boolean"}}, "required": [], "additionalProperties": False}

    def execute(self, args, request):
        from surveys.models import Survey
        qs = Survey.objects.all()
        if 'is_active' in args:
            qs = qs.filter(is_active=args['is_active'])
        return {"surveys": [{"id": str(s.id), "title": s.title, "is_active": s.is_active, "response_count": s.response_count, "start_date": str(s.start_date) if s.start_date else None, "end_date": str(s.end_date) if s.end_date else None} for s in qs]}


@register_tool
class CreateSurvey(AssistantTool):
    name = "create_survey"
    description = "Create a survey with questions."
    module_id = "surveys"
    required_permission = "surveys.add_survey"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "title": {"type": "string"}, "description": {"type": "string"},
            "start_date": {"type": "string"}, "end_date": {"type": "string"},
            "questions": {"type": "array", "items": {"type": "object", "properties": {"text": {"type": "string"}, "question_type": {"type": "string"}, "is_required": {"type": "boolean"}}, "required": ["text"]}},
        },
        "required": ["title"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from surveys.models import Survey, SurveyQuestion
        s = Survey.objects.create(title=args['title'], description=args.get('description', ''), start_date=args.get('start_date'), end_date=args.get('end_date'))
        for i, q in enumerate(args.get('questions', [])):
            SurveyQuestion.objects.create(survey=s, text=q['text'], question_type=q.get('question_type', 'text'), is_required=q.get('is_required', False), order=i)
        return {"id": str(s.id), "title": s.title, "questions_count": len(args.get('questions', [])), "created": True}
