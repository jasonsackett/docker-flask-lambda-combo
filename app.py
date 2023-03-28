from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def flask_route():
    """
    flask endpoint example
    """
    args = "{}"  # just to handle 'GET' (with no request.data)
    if len(request.data) > 0:
        args = request.data
    return work(json.loads(args))


def handler(event, context):
    """
    AWS Lambda handler
    """
    return work(event)


def work(args):
    return f'doing work on job_id: {args.get("job_id", 0)}'


if __name__ == "__main__":
    _run_as_flask = False
    _job_id = 1234
    if _run_as_flask:
        app.run(debug=True)
    else:
        # example usage of aws lambda handler
        _ret = handler({'job_id': _job_id}, None)
        print(f'main, {_ret}')
