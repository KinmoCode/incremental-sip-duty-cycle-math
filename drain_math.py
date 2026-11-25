#!/usr/bin/env python3
"""Harmonic cycle throughput calculator for Drink the Ocean."""
import json, sys

def calc_throughput(sip_rate: float, tank_cap: float, trip_sec: float = 6.5, players: int = 1) -> dict:
    t_sip = tank_cap / max(sip_rate, 0.001)
    net_lps = (players * tank_cap) / (t_sip + trip_sec)
    duty = t_sip / (t_sip + trip_sec)
    bottleneck = "Press-Trip-Bound (Upgrade Bigger Belly first)" if duty < 0.38 else (
        "Sip-Bound (Upgrade Extra Straws / Mouth Vacuum / Whirlpool)" if duty > 0.62 else "Balanced Harmonic Window"
    )
    return {
        "players": players,
        "t_sip_sec": round(t_sip, 2),
        "t_trip_sec": trip_sec,
        "duty_cycle_pct": round(duty * 100, 1),
        "net_liters_per_sec": round(net_lps, 2),
        "bottleneck": bottleneck,
    }

if __name__ == "__main__":
    sr = float(sys.argv[1]) if len(sys.argv) > 1 else 25.0
    tc = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
    pl = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    print(json.dumps(calc_throughput(sr, tc, 6.5, pl), indent=2))
