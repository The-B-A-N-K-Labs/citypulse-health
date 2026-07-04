from app.agents.coordinating_agent import CoordinatingAgent
from app.services.data_loader import DataLoader
from app.agents.health_agent import get_city_summary, get_anomalies


class MorningBriefingWorkflow:
    """Orchestrates the morning briefing experience."""

    def __init__(self) -> None:
        self.data_loader = DataLoader()
        self.coordinator = CoordinatingAgent()

    def generate_briefing(self) -> dict:
        # Dynamically fetches the freshest live data from BigQuery
        context = self.data_loader.load_sample_data()
        result = self.coordinator.run(context)
        live_summary = get_city_summary()
        live_anomalies = get_anomalies()

        return {
            "morning_briefing": result["summary"],
            "explanation": result["explanation"],
            "actions": result["actions"],
            "anomalies": live_anomalies.get("anomalies", []),
            "summary": live_summary
        }
