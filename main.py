import argparse
from agents.data_agent import DataAgent
from agents.plot_agent import PlotAgent
from agents.analysis_agent import AnalysisAgent

def main(input_path):
    data_agent = DataAgent(input_path)
    x, y = data_agent.load()

    plot_agent = PlotAgent()
    fig_path = plot_agent.plot(x, y)

    analysis_agent = AnalysisAgent()
    report = analysis_agent.analyze(x, y)

    print("=== Analysis Report ===")
    print(report)
    print(f"Figure saved to: {fig_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    main(args.input)
