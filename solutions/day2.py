from dataclasses import dataclass

TEST_POLICY = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

TEST_TARGET = (True, False, True)


@dataclass
class Policy:
    min_count: int
    max_count: int
    letter: str


def parse_policy(raw_policy):
    for line in raw_policy:
        policy = Policy(
            int(line.split("-")[0]),
            int(line.split("-")[1].split(" ")[0]),
            line.split(":")[0].split(" ")[1],
        )
        password = line.split(":")[1].strip()
        yield policy, password


def validate_password(policy: Policy, password: str):
    if policy.min_count <= password.count(policy.letter) <= policy.max_count:
        return True
    else:
        return False


assert next(parse_policy(TEST_POLICY.splitlines())) == (Policy(1, 3, "a"), "abcde")

assert all(
    val == targ
    for val, targ in zip(
        (
            validate_password(policy, password)
            for policy, password in parse_policy(TEST_POLICY.splitlines())
        ),
        TEST_TARGET,
    )
)

TEST_TARGET = (True, False, False)

def validate_toboggan_password(policy: Policy, password: str):
    if (len(password) < policy.min_count) or (len(password) < policy.max_count):
        return False
    elif (password[policy.min_count-1] == policy.letter) != (password[policy.max_count-1] == policy.letter):
        return True
    else:
        return False

assert all(
    val == targ
    for val, targ in zip(
        (
            validate_toboggan_password(policy, password)
            for policy, password in parse_policy(TEST_POLICY.splitlines())
        ),
        TEST_TARGET,
    )
)


with open("inputs/day2.txt", "r") as infile:
    print(
        sum(
            validate_password(policy, password)
            for policy, password in parse_policy(infile)
        )
    )
    
with open("inputs/day2.txt", "r") as infile:
    print(
        sum(
            validate_toboggan_password(policy, password)
            for policy, password in parse_policy(infile)
        )
    )
