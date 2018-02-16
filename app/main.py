from flask import Flask, Response, request

from sphttp import Downloader, DelayRequestAlgorithm, DuplicateRequestAlgorithm

app = Flask(__name__)


@app.route('/proxy')
def proxy():

    hosts = request.args.get('hosts').split(',')
    split_size = int(request.args.get('split_size', 10**6))
    enable_trace_log = bool(request.args.get('enable_trace_log', False))
    verify = bool(request.args.get('verify', 'true'))
    delay_req_algo = eval(request.args.get('delay_req_algo',
                                           'DelayRequestAlgorithm.DIFF'))
    enable_dup_req = bool(request.args.get('enable_dup_req', True))
    dup_req_algo = eval(request.args.get('dup_req_algo',
                                         'DuplicateRequestAlgorithm.IBRC'))
    close_bad_conn = bool(request.args.get('close_bad_conn', False))
    static_delay_req_vals = request.args.get('static_delay_req_vals', None)
    enable_init_delay = bool(request.args.get('enable_init_delay', True))
    invalid_block_threshold = int(request.args.get('invalid_block_threshold',
                                                   20))
    init_delay_coef = float(request.args.get('init_delay_coef', 10))

    d = Downloader(urls=hosts,
                   split_size=split_size,
                   enable_trace_log=enable_trace_log,
                   verify=verify,
                   delay_req_algo=delay_req_algo,
                   enable_dup_req=enable_dup_req,
                   dup_req_algo=dup_req_algo,
                   close_bad_conn=close_bad_conn,
                   static_delay_req_vals=static_delay_req_vals,
                   enable_init_delay=enable_init_delay,
                   invalid_block_threshold=invalid_block_threshold,
                   init_delay_coef=init_delay_coef,)

    return Response(d.generator(), mimetype='application/octet-stream')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
