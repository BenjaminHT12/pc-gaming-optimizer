import random
import time
import itertools
import math
import json

random.seed(42)

# ============================================================
# DATA KOMPONEN PC GAMING (DUMMY REALISTIS)
# ============================================================

components = {
    "CPU": [
        {"name": "AMD Ryzen 5 5600X", "price": 1850000, "performance": 82},
        {"name": "Intel Core i5-12400F", "price": 1750000, "performance": 80},
        {"name": "AMD Ryzen 7 5700X", "price": 2500000, "performance": 89},
        {"name": "Intel Core i5-13400F", "price": 2100000, "performance": 85},
        {"name": "AMD Ryzen 5 5500", "price": 1200000, "performance": 72},
        {"name": "Intel Core i3-12100F", "price": 950000, "performance": 65},
        {"name": "AMD Ryzen 9 5900X", "price": 3800000, "performance": 96},
        {"name": "Intel Core i7-12700F", "price": 3200000, "performance": 93},
        {"name": "AMD Ryzen 5 4600G", "price": 1400000, "performance": 70},
        {"name": "Intel Core i5-10400F", "price": 850000, "performance": 62},
        {"name": "AMD Ryzen 7 5800X", "price": 2900000, "performance": 91},
        {"name": "Intel Core i9-12900K", "price": 5500000, "performance": 98},
    ],
    "GPU": [
        {"name": "NVIDIA RTX 3060", "price": 3500000, "performance": 80},
        {"name": "NVIDIA RTX 3060 Ti", "price": 4500000, "performance": 87},
        {"name": "AMD RX 6600", "price": 2900000, "performance": 75},
        {"name": "NVIDIA RTX 3070", "price": 6000000, "performance": 92},
        {"name": "AMD RX 6650 XT", "price": 3200000, "performance": 78},
        {"name": "NVIDIA GTX 1660 Super", "price": 2200000, "performance": 65},
        {"name": "AMD RX 6700 XT", "price": 5000000, "performance": 88},
        {"name": "NVIDIA RTX 3050", "price": 2000000, "performance": 60},
        {"name": "AMD RX 6500 XT", "price": 1500000, "performance": 52},
        {"name": "NVIDIA RTX 4060", "price": 5200000, "performance": 90},
        {"name": "AMD RX 7600", "price": 4100000, "performance": 83},
        {"name": "NVIDIA RTX 3080", "price": 8000000, "performance": 96},
    ],
    "RAM": [
        {"name": "Corsair 16GB DDR4 3200", "price": 650000, "performance": 80},
        {"name": "G.Skill 16GB DDR4 3600", "price": 800000, "performance": 88},
        {"name": "Kingston 8GB DDR4 3200", "price": 320000, "performance": 60},
        {"name": "Kingston 32GB DDR4 3200", "price": 1200000, "performance": 90},
        {"name": "Crucial 16GB DDR4 3200", "price": 620000, "performance": 78},
        {"name": "G.Skill 32GB DDR5 6000", "price": 2200000, "performance": 95},
        {"name": "Corsair 8GB DDR4 2666", "price": 280000, "performance": 55},
        {"name": "TeamGroup 16GB DDR4 3200", "price": 580000, "performance": 76},
        {"name": "Adata 16GB DDR4 3600", "price": 700000, "performance": 82},
        {"name": "XPG 32GB DDR4 3600", "price": 1500000, "performance": 92},
        {"name": "Crucial 32GB DDR5 4800", "price": 1800000, "performance": 93},
        {"name": "Kingston 8GB DDR4 2400", "price": 250000, "performance": 50},
    ],
    "Storage": [
        {"name": "Samsung 980 500GB NVMe", "price": 750000, "performance": 88},
        {"name": "WD Black SN770 1TB", "price": 1100000, "performance": 92},
        {"name": "Kingston NV2 1TB NVMe", "price": 800000, "performance": 82},
        {"name": "Seagate 1TB HDD 7200", "price": 350000, "performance": 45},
        {"name": "Crucial P3 1TB NVMe", "price": 850000, "performance": 80},
        {"name": "Samsung 870 EVO 500GB SATA", "price": 650000, "performance": 70},
        {"name": "WD Blue SN570 500GB", "price": 600000, "performance": 78},
        {"name": "Adata Legend 960 2TB", "price": 1500000, "performance": 90},
        {"name": "Seagate Barracuda 2TB HDD", "price": 550000, "performance": 42},
        {"name": "SK Hynix P41 1TB NVMe", "price": 1200000, "performance": 94},
        {"name": "Samsung 980 Pro 1TB", "price": 1400000, "performance": 96},
        {"name": "XPG SX8200 Pro 512GB", "price": 700000, "performance": 85},
    ],
    "Motherboard": [
        {"name": "MSI B550M Pro-VDH", "price": 1200000, "performance": 72},
        {"name": "Asus ROG Strix B550-F", "price": 2500000, "performance": 90},
        {"name": "Gigabyte B660M DS3H", "price": 1100000, "performance": 70},
        {"name": "MSI Pro B660M-A", "price": 1300000, "performance": 74},
        {"name": "Asus Prime B550-Plus", "price": 1600000, "performance": 80},
        {"name": "Gigabyte X570 Aorus Elite", "price": 2800000, "performance": 92},
        {"name": "MSI MAG B550 Tomahawk", "price": 1900000, "performance": 85},
        {"name": "ASRock B550M Pro4", "price": 1100000, "performance": 71},
        {"name": "Asus TUF B560M-Plus", "price": 1400000, "performance": 76},
        {"name": "Gigabyte B660M Pro RS", "price": 1250000, "performance": 73},
        {"name": "MSI MEG Z690 Ace", "price": 4500000, "performance": 97},
        {"name": "Asus ROG Maximus Z690", "price": 5500000, "performance": 99},
    ],
    "PSU": [
        {"name": "Seasonic Focus GX 650W", "price": 1200000, "performance": 90},
        {"name": "Corsair CV550 550W", "price": 700000, "performance": 70},
        {"name": "FSP HYPER 600W", "price": 650000, "performance": 68},
        {"name": "EVGA SuperNOVA 750W G6", "price": 1400000, "performance": 92},
        {"name": "be quiet! Pure Power 11 600W", "price": 900000, "performance": 80},
        {"name": "Cooler Master MWE 650W Bronze", "price": 800000, "performance": 72},
        {"name": "Antec NeoECO 650W", "price": 750000, "performance": 74},
        {"name": "Thermaltake Smart 700W", "price": 700000, "performance": 69},
        {"name": "Seasonic Focus GX 750W", "price": 1400000, "performance": 92},
        {"name": "Corsair RM750x", "price": 1600000, "performance": 94},
        {"name": "be quiet! Straight Power 11 750W", "price": 1500000, "performance": 93},
        {"name": "DeepCool PQ650M", "price": 750000, "performance": 75},
    ],
}

# Skenario budget mahasiswa
budgets = {
    "Budget Ketat (4 juta)": 4_000_000,
    "Budget Sedang (8 juta)": 8_000_000,
    "Budget Longgar (15 juta)": 15_000_000,
}

# ============================================================
# ALGORITMA 1: GREEDY
# ============================================================

def greedy_selection(budget, components):
    """
    Greedy: pilih komponen dengan rasio performance/price tertinggi
    yang masih muat dalam budget sisa.
    """
    remaining = budget
    selected = {}
    total_perf = 0

    for comp_type, items in components.items():
        affordable = [item for item in items if item["price"] <= remaining]
        if not affordable:
            # Pilih yang termurah
            chosen = min(items, key=lambda x: x["price"])
        else:
            # Greedy: maximize performance per rupiah
            chosen = max(affordable, key=lambda x: x["performance"] / x["price"])
        selected[comp_type] = chosen
        remaining -= chosen["price"]
        total_perf += chosen["performance"]

    total_cost = sum(c["price"] for c in selected.values())
    return selected, total_cost, total_perf / len(components)


# ============================================================
# ALGORITMA 2: BRANCH AND BOUND
# ============================================================

def upper_bound(remaining_budget, remaining_types, components):
    """Hitung upper bound: ambil item dengan performance/price terbaik per kategori."""
    ub = 0
    rem = remaining_budget
    for comp_type in remaining_types:
        affordable = [item for item in components[comp_type] if item["price"] <= rem]
        if affordable:
            best = max(affordable, key=lambda x: x["performance"] / x["price"])
            ub += best["performance"]
            rem -= best["price"]
        else:
            best = min(components[comp_type], key=lambda x: x["price"])
            ub += best["performance"]
    return ub


def branch_and_bound(budget, components):
    """
    Branch and Bound untuk optimasi pemilihan komponen PC.
    State: (current_cost, current_perf_sum, selected_dict, remaining_types)
    """
    comp_types = list(components.keys())
    best_perf = [0]
    best_selection = [{}]
    nodes_explored = [0]

    def bb_recursive(idx, cost, perf_sum, current_selection):
        nodes_explored[0] += 1
        if idx == len(comp_types):
            if cost <= budget:
                avg = perf_sum / len(comp_types)
                if avg > best_perf[0]:
                    best_perf[0] = avg
                    best_selection[0] = dict(current_selection)
            return

        comp_type = comp_types[idx]
        remaining_types = comp_types[idx+1:]

        for item in components[comp_type]:
            new_cost = cost + item["price"]
            if new_cost > budget:
                continue
            new_perf = perf_sum + item["performance"]
            # Upper bound pruning
            ub = new_perf + upper_bound(budget - new_cost, remaining_types, components)
            avg_ub = ub / len(comp_types)
            if avg_ub <= best_perf[0]:
                continue  # Prune
            current_selection[comp_type] = item
            bb_recursive(idx+1, new_cost, new_perf, current_selection)
            del current_selection[comp_type]

    bb_recursive(0, 0, 0, {})

    if not best_selection[0]:
        # Fallback ke greedy jika B&B tidak menemukan solusi valid
        sel, cost, perf = greedy_selection(budget, components)
        return sel, cost, perf, nodes_explored[0]

    total_cost = sum(c["price"] for c in best_selection[0].values())
    return best_selection[0], total_cost, best_perf[0], nodes_explored[0]


# ============================================================
# ALGORITMA 3: GENETIC ALGORITHM
# ============================================================

def create_individual(components):
    """Buat kromosom random: indeks komponen untuk setiap tipe."""
    return {ct: random.randint(0, len(items)-1) for ct, items in components.items()}

def decode_individual(individual, components):
    """Decode kromosom menjadi dict komponen."""
    return {ct: components[ct][idx] for ct, idx in individual.items()}

def fitness(individual, components, budget):
    """Fitness = rata-rata performance jika dalam budget, else penalti."""
    sel = decode_individual(individual, components)
    cost = sum(item["price"] for item in sel.values())
    perf = sum(item["performance"] for item in sel.values()) / len(components)
    if cost > budget:
        excess_ratio = (cost - budget) / budget
        return max(0, perf - 50 * excess_ratio)
    return perf

def crossover(p1, p2, components):
    """Single-point crossover pada level komponen."""
    comp_types = list(components.keys())
    point = random.randint(1, len(comp_types)-1)
    child1 = {}
    child2 = {}
    for i, ct in enumerate(comp_types):
        if i < point:
            child1[ct] = p1[ct]
            child2[ct] = p2[ct]
        else:
            child1[ct] = p2[ct]
            child2[ct] = p1[ct]
    return child1, child2

def mutate(individual, components, mutation_rate=0.15):
    """Random mutation: ganti indeks komponen secara acak."""
    for ct, items in components.items():
        if random.random() < mutation_rate:
            individual[ct] = random.randint(0, len(items)-1)
    return individual

def genetic_algorithm(budget, components, pop_size=60, generations=100):
    """
    Genetic Algorithm untuk optimasi pemilihan komponen PC.
    """
    gen_evaluations = []
    # Inisialisasi populasi
    population = [create_individual(components) for _ in range(pop_size)]

    best_overall = None
    best_fitness = -1

    for gen in range(generations):
        # Evaluasi fitness
        scored = [(ind, fitness(ind, components, budget)) for ind in population]
        scored.sort(key=lambda x: -x[1])

        if scored[0][1] > best_fitness:
            best_fitness = scored[0][1]
            best_overall = scored[0][0]

        gen_evaluations.append(scored[0][1])

        # Elitisme: top 10%
        elite_count = max(2, pop_size // 10)
        new_pop = [ind for ind, _ in scored[:elite_count]]

        # Crossover & mutasi
        while len(new_pop) < pop_size:
            p1, p2 = random.choices(scored[:pop_size//2], k=2)
            c1, c2 = crossover(p1[0], p2[0], components)
            new_pop.append(mutate(c1, components))
            if len(new_pop) < pop_size:
                new_pop.append(mutate(c2, components))

        population = new_pop

    # Decode solusi terbaik
    best_sel = decode_individual(best_overall, components)
    total_cost = sum(item["price"] for item in best_sel.values())
    avg_perf = sum(item["performance"] for item in best_sel.values()) / len(components)

    return best_sel, total_cost, avg_perf, gen_evaluations


# ============================================================
# EKSPERIMEN UTAMA
# ============================================================

print("=" * 65)
print("EKSPERIMEN: OPTIMASI KOMPONEN PC GAMING")
print("=" * 65)

results_summary = {}

for budget_name, budget_val in budgets.items():
    print(f"\n{'='*65}")
    print(f"SKENARIO: {budget_name} (Rp {budget_val:,})")
    print(f"{'='*65}")
    results_summary[budget_name] = {}

    # --- GREEDY ---
    t0 = time.perf_counter()
    g_sel, g_cost, g_perf = greedy_selection(budget_val, components)
    t1 = time.perf_counter()
    g_time = (t1 - t0) * 1000

    print(f"\n[GREEDY]")
    print(f"  Total Biaya  : Rp {g_cost:,}")
    print(f"  Avg Perf     : {g_perf:.2f}")
    print(f"  Waktu        : {g_time:.3f} ms")
    for ct, item in g_sel.items():
        print(f"    {ct:12s}: {item['name']} (Rp {item['price']:,}, Perf {item['performance']})")

    results_summary[budget_name]["greedy"] = {
        "cost": g_cost, "perf": round(g_perf, 2), "time_ms": round(g_time, 4)
    }

    # --- BRANCH AND BOUND ---
    t0 = time.perf_counter()
    bb_sel, bb_cost, bb_perf, bb_nodes = branch_and_bound(budget_val, components)
    t1 = time.perf_counter()
    bb_time = (t1 - t0) * 1000

    print(f"\n[BRANCH AND BOUND]")
    print(f"  Total Biaya  : Rp {bb_cost:,}")
    print(f"  Avg Perf     : {bb_perf:.2f}")
    print(f"  Waktu        : {bb_time:.3f} ms")
    print(f"  Node Dijelajahi: {bb_nodes:,}")
    for ct, item in bb_sel.items():
        print(f"    {ct:12s}: {item['name']} (Rp {item['price']:,}, Perf {item['performance']})")

    results_summary[budget_name]["bnb"] = {
        "cost": bb_cost, "perf": round(bb_perf, 2), "time_ms": round(bb_time, 4), "nodes": bb_nodes
    }

    # --- GENETIC ALGORITHM ---
    t0 = time.perf_counter()
    ga_sel, ga_cost, ga_perf, ga_conv = genetic_algorithm(budget_val, components)
    t1 = time.perf_counter()
    ga_time = (t1 - t0) * 1000

    print(f"\n[GENETIC ALGORITHM]")
    print(f"  Total Biaya  : Rp {ga_cost:,}")
    print(f"  Avg Perf     : {ga_perf:.2f}")
    print(f"  Waktu        : {ga_time:.3f} ms")
    print(f"  Generasi     : 100, Pop Size: 60")
    for ct, item in ga_sel.items():
        print(f"    {ct:12s}: {item['name']} (Rp {item['price']:,}, Perf {item['performance']})")

    results_summary[budget_name]["ga"] = {
        "cost": ga_cost, "perf": round(ga_perf, 2), "time_ms": round(ga_time, 4),
        "convergence": [round(v, 2) for v in ga_conv]
    }

# Save results
with open("experiment_results.json", "w") as f:
    json.dump(results_summary, f, indent=2)

print("\n\n" + "="*65)
print("RINGKASAN PERBANDINGAN")
print("="*65)
for bname, res in results_summary.items():
    print(f"\n{bname}:")
    print(f"  {'Algoritma':<20} {'Biaya (Rp)':>15} {'Avg Perf':>10} {'Waktu (ms)':>12}")
    print(f"  {'-'*60}")
    for alg, label in [("greedy", "Greedy"), ("bnb", "Branch & Bound"), ("ga", "Genetic Algo")]:
        d = res[alg]
        print(f"  {label:<20} {d['cost']:>15,} {d['perf']:>10.2f} {d['time_ms']:>12.3f}")

print("\nEksperimen selesai. Hasil disimpan di experiment_results.json")
