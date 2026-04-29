import matplotlib.pyplot as plt

class PlotAgent:
    def plot(self, x, y):
        plt.figure(figsize=(6,4))
        plt.plot(x, y)
        plt.xlabel("Wavelength")
        plt.ylabel("Intensity")
        plt.title("Spectrum")
        plt.tight_layout()
        path = "output.png"
        plt.savefig(path, dpi=300)
        return path
