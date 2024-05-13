"""
Object classes to fake data
"""

import math
import random
from datetime import timedelta
from faker import Faker


class FakeInfo:
    """
    FakeInfo class
    """

    def __init__(self):
        self.fake = Faker()
        self.fake_names = [self.fake.name() for _ in range(100)]
        self.fake_contacts_ids = [random.randint(1000, 9999) for _ in range(100)]
        self.fake_durations = [
            timedelta(minutes=random.randint(3, 9), seconds=random.randint(0, 59))
            for _ in range(100)
        ]
        self.fake_asas = [
            timedelta(minutes=random.randint(0, 5), seconds=random.randint(0, 59))
            for _ in range(100)
        ]
        self.fake_bad_service_levels = [random.randint(20, 60) for _ in range(100)]
        self.fake_good_service_levels = [random.randint(80, 99) for _ in range(100)]

    def format_timedelta(self, td: timedelta) -> str:
        """
        Format timedelta to minutes and seconds like mm:ss
        """
        minutes, seconds = divmod(td.total_seconds(), 60)
        return f"{int(minutes):02}:{int(seconds):02}"

    def fake_info(self, alert_id, resource_type, is_solved):
        """
        Fake agent info
        """

        acr, asa, fcr, adherence = 0, 0, 0, 0
        acr_color, asa_color, fcr_color, adherence_color = (
            "red",
            "red",
            "red",
            "yellow",
        )

        if is_solved:
            acr = random.randint(10, 20)
            acr_color = "green"
            asa = f"{random.randint(0, 2)}:{random.randint(0, 59)} min"
            asa_color = "green"
            fcr = random.randint(70, 80)
            fcr_color = "green"
            adherence = random.randint(60, 80)
        else:
            acr = random.randint(40, 70)
            asa = f"{random.randint(7, 9)}:{random.randint(0, 59)} min"
            fcr = random.randint(5, 20)
            adherence = random.randint(10, 50)

        ##################################### ROUTING PROFILE ######################################
        if resource_type == "routing-profile":

            return [
                {
                    "title": "Information",
                    "elements": [
                        {"title": "Alias", "content": "Support", "color": "black"},
                        {"title": "Created at", "content": "5-1-24", "color": "black"},
                        {"title": "Total agents", "content": "30", "color": "black"},
                    ],
                },
                {
                    "title": "Metrics",
                    "elements": [
                        {
                            "title": "Service Level",
                            "content": f"{self.fake_good_service_levels[alert_id] + random.randint(-1,1) if is_solved else self.fake_bad_service_levels[alert_id] + random.randint(-1,1)}",
                            "color": "green" if is_solved else "red",
                        },
                        {"title": "ACR", "content": f"{acr}", "color": f"{acr_color}"},
                        {"title": "ASA", "content": f"{asa}", "color": f"{asa_color}"},
                        {"title": "FCR", "content": f"{fcr}", "color": f"{fcr_color}"},
                        {
                            "title": "Adherence",
                            "content": f"{adherence}",
                            "color": f"{adherence_color}",
                        },
                    ],
                },
            ]
        ######################################## QUEUE ########################################
        elif resource_type == "queue":
            total_agents = random.randint(2, 12)
            active_agents = 0
            if is_solved:
                active_agents = random.randint(2, math.floor(total_agents / 3))
            else:
                active_agents = random.randint(
                    math.floor(total_agents / 2), total_agents
                )
            active_agents_color = "green"
            if active_agents > total_agents * 0.8:
                active_agents_color = "red"
            elif active_agents > total_agents * 0.5:
                active_agents_color = "yellow"

            return [
                {
                    "title": "Information",
                    "elements": [
                        {"title": "Alias", "content": "Text Chats", "color": "black"},
                        {"title": "Created at", "content": "5-1-24", "color": "black"},
                        {
                            "title": "Total agents",
                            "content": f"{total_agents}",
                            "color": "black",
                        },
                        {"title": "Skill", "content": "Support", "color": "black"},
                        {
                            "title": "Contacts",
                            "content": f"{active_agents}/{total_agents}",
                            "color": f"{active_agents_color}",
                        },
                    ],
                },
                {
                    "title": "Metrics",
                    "elements": [
                        {
                            "title": "Service Level",
                            "content": f"{self.fake_good_service_levels[alert_id] + random.randint(-1,1) if is_solved else self.fake_bad_service_levels[alert_id] + random.randint(-1,1)}",
                            "color": "green" if is_solved else "red",
                        },
                        {"title": "ACR", "content": f"{acr}", "color": f"{acr_color}"},
                        {"title": "ASA", "content": f"{asa}", "color": f"{asa_color}"},
                        {"title": "FCR", "content": f"{fcr}", "color": f"{fcr_color}"},
                        {
                            "title": "Adherence",
                            "content": f"{adherence}",
                            "color": f"{adherence_color}",
                        },
                    ],
                },
            ]
        ######################################## AGENT ########################################
        elif resource_type == "agent":
            # add a second to the duration
            self.fake_durations[alert_id] += timedelta(seconds=1)
            self.fake_asas[alert_id] += timedelta(seconds=random.randint(-1, 1))
            return [
                {
                    "title": "Information",
                    "elements": [
                        {
                            "title": "Name",
                            "content": f"{self.fake_names[alert_id]}",
                            "color": "black",
                        },
                        {"title": "Skill", "content": "Support", "color": "black"},
                        {
                            "title": "Status",
                            "content": "On Call",
                            "color": "red",
                        },
                    ],
                },
                {
                    "title": "Contact Information",
                    "elements": [
                        {
                            "title": "ID",
                            "content": f"{self.fake_contacts_ids[alert_id]}",
                            "color": "black",
                        },
                        {
                            "title": "Duration",
                            "content": f"{ self.format_timedelta(self.fake_durations[alert_id])} min",
                            "color": "red",
                        },
                        {
                            "title": "Emotion",
                            "content": "POSITIVE" if is_solved else "NEGATIVE",
                            "color": "green" if is_solved else "red",
                        },
                    ],
                },
                {
                    "title": "Metrics",
                    "elements": [
                        {
                            "title": "Service Level",
                            "content": f"{self.fake_good_service_levels[alert_id] + random.randint(-1,1) if is_solved else self.fake_bad_service_levels[alert_id] + random.randint(-1,1)}",
                            "color": "green" if is_solved else "red",
                        },
                        {"title": "ACR", "content": f"{acr}", "color": f"{acr_color}"},
                        {"title": "ASA", "content": f"{ self.format_timedelta(self.fake_asas[alert_id]) } min", "color": "yellow"},
                        {"title": "FCR", "content": f"{fcr}", "color": f"{fcr_color}"},
                        {
                            "title": "Adherence",
                            "content": f"{adherence}",
                            "color": f"{adherence_color}",
                        },
                    ],
                },
            ]
        else:
            raise ValueError("Invalid type")
