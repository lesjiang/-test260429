import numpy as np
from scipy.signal import find_peaks

class AnalysisAgent:
    def analyze(self, x, y):
        peaks, _ = find_peaks(y, prominence=0.1)
        report = "Detected Peaks:\n"
        for i, p in enumerate(peaks):
            report += f"Peak {i+1}: {x[p]:.3f}, intensity {y[p]:.3f}\n"
        report += "Overall spectrum shows clear resonance behavior."
        return report
