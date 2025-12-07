import os
import time

start_time = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"

with open(file, encoding="utf-8") as f:
    data = f.read().splitlines()


def mix(a, b):
    return a ^ b


def prune(secret_number):
    return secret_number % 16777216


def evolves(secret_number):
    secret_number = prune(mix(secret_number, secret_number * 64))
    secret_number = prune(mix(secret_number, secret_number // 32))
    secret_number = prune(mix(secret_number, secret_number * 2048))
    return secret_number


def n_evolves(secret_number, n):
    for _ in range(n):
        secret_number = evolves(secret_number)
    return secret_number


# for i in range(2000):
#     data = [evolves(int(x)) for x in data]

# print(sum(data))

secrets = [n_evolves(int(x), 2000) for x in data]
print("Part 1:", sum(secrets))


print("Time taken: " + str(round(time.time() - start_time, 3)) + "s")

## part 2


def get_all_secrets(data, n):
    secrets = []
    for d in data:
        d_secrets = [int(d)]
        for _ in range(n):
            d_secrets.append(evolves(d_secrets[-1]))
        secrets.append(d_secrets)
    return secrets


secrets_all = get_all_secrets(data, 2000)


def prices_by_monkeys(secrets):
    prices = {}
    secrets = list(map(lambda x: x % 10, secrets))
    for i in range(4, 2001):
        price_deltas = (
            secrets[i - 3] - secrets[i - 4],
            secrets[i - 2] - secrets[i - 3],
            secrets[i - 1] - secrets[i - 2],
            secrets[i] - secrets[i - 1],
        )
        if price_deltas not in prices:
            prices[price_deltas] = secrets[i]

    return prices


prices_var = {}
for list_secrets in secrets_all:
    for prices, value in prices_by_monkeys(list_secrets).items():
        prices_var[prices] = prices_var.get(prices, 0) + value

print("Part 2:", max(prices_var.values()))


print("Time taken: " + str(round(time.time() - start_time, 3)) + "s")
