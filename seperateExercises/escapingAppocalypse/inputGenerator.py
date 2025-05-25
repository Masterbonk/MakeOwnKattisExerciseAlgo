import random

def generate_input(
    test_cases=100,
    min_nodes=1000, max_nodes=1000,
    max_people=100,
    max_time_steps=100,
    max_hospitals=1000,
    max_roads=1000,
    max_road_capacity=100,
    max_road_time=100
):
    input_lines = []
    input_lines.append(str(test_cases))
    
    for _ in range(test_cases):
        n = random.randint(min_nodes, max_nodes)
        input_lines.append(str(n))

        start_location = random.randint(1, n)
        people = max_people
        steps = max_time_steps
        input_lines.append(f"{start_location} {people} {steps}")

        m = min(max_hospitals, n)
        hospital_locations = random.sample(range(1, n+1), m)
        input_lines.append(str(m))
        input_lines.extend(str(h) for h in hospital_locations)

        r = max_roads
        input_lines.append(str(r))

        existing_roads = set()
        for _ in range(r):
            while True:
                a = random.randint(1, n)
                b = random.randint(1, n)
                if a != b and (a, b) not in existing_roads:
                    existing_roads.add((a, b))
                    break
            p = random.randint(1, max_road_capacity)
            t = random.randint(1, max_road_time)
            input_lines.append(f"{a} {b} {p} {t}")
    
    return "\n".join(input_lines)

# Example usage
with open("test_input.txt", "w") as f:
    f.write(generate_input())

