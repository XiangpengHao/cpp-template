import json


def process():
    data = {}
    with open('data.json') as f:
        data = json.load(f)
        lines = []
        with open('bench_data') as bench:
            lines = bench.readlines()[0]
            lines = lines.split(' ')

        data['data'].append({
            'gitTag': lines[0],
            'buildId': int(lines[1]),
            'dataPoint': int(lines[2])
        })

    with open('data.json', 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    process()
