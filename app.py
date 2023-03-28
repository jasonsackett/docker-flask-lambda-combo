from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """
    flask endpoint example
    """
    return f'Hello, World!'


@app.route('/hellox/<x>')
def hellox(x):
    """
    flask endpoint example
    """
    return f'Hello, World! {x}'


def handler(event, context):
    """
    AWS Lambda handler, default
    """
    job_id = event.get("job_id", None)
    ret = hellox(job_id)
    print('from handler')
    return ret


if __name__ == "__main__":
    _run_as_flask = False
    _job_id = 239311
    if _run_as_flask:
        app.run(debug=True)
    else:
        # example usage of aws lambda handler
        _ret = handler({'job_id': _job_id}, None)
        print(f'main, {_ret}')
