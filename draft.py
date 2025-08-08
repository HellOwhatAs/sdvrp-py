import sdvrp_py
import matplotlib.pyplot as plt


def run_instance(path: str):
    with open(path, "r") as f:
        [[_, capacity], demands, *data] = [
            [int(j) for j in i.strip().split()] for i in f.readlines() if i.strip()
        ]

    data = [[j * 1000 for j in i] for i in data]

    res = sdvrp_py.solve_sdvrp(
        capacity=capacity,
        demands=demands,
        coord_list=data,
        time_limit=10,
    )

    res = [[j for j in i if j[1] > 0] for i in res]
    for row in res:
        print(row)

    fig = plt.figure()
    plt.scatter(
        [i[0] for i in data],
        [i[1] for i in data],
        color="blue",
        label="Customers",
    )
    for route in res:
        x = [data[0][0], *(data[j][0] for j, _ in route), data[0][0]]
        y = [data[0][1], *(data[j][1] for j, _ in route), data[0][1]]
        plt.plot(x, y, marker=None)

    return fig


if __name__ == "__main__":
    import glob
    from tqdm import tqdm

    for path in tqdm(
        [
            i
            for i in glob.glob("../Alkaid-SDVRP/data/SET-*/*.*")
            if not i.endswith(".pdf")
        ]
    ):
        print(path)
        fig = run_instance(path)
        fig.savefig(path[: path.rfind(".")] + ".pdf")
