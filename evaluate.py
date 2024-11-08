from azure.ai.evaluation import evaluate
from opentelemetry import trace

tracer = trace.get_tracer(__name__)


def exact_match(response: str, truth: str, **kwargs):
    score = 1 if response.lower() == truth.lower() else 0
    return {"score": score}


class Experiment:

    def __init__(self):
        pass

    def __call__(self, line: int, query: str, **kwargs):
        # This span does not show up in the AML workspace. I see the Experiment trace but can't open it further to see the nested span
        # It does show up in the local tracing experience. 
        with tracer.start_as_current_span("test_span", attributes={"query": query}):
            # mock responses
            if line == 0:
                mock_response = "The capital of France is Paris"
            else: 
                mock_response = "I don't know."
            return {"response": mock_response}



if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    from pprint import pprint
    load_dotenv()

    evaluators = {
        "exact_match": exact_match,
    }
    evaluator_config = {
        "exact_match": {
            "response": "${target.response}",
            "truth": "${data.truth}"
        }
    }

    target = Experiment()

    result = evaluate(
        evaluation_name="test-2",
        data="evaluate_test_data.jsonl",
        target=target,
        evaluators=evaluators,
        evaluator_config=evaluator_config,
        azure_ai_project={
            "subscription_id": os.environ.get("SUBSCRIPTION_ID"),
            "resource_group_name": os.environ.get("RESOURCE_GROUP_NAME"),
            "project_name": os.environ.get("WORKSPACE_NAME"),
        }
    )

    pprint(result)