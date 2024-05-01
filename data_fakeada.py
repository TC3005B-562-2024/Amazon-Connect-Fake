"""
Object classes to fake data
"""

import math
import random
from faker import Faker


class FakeInfo:
    """
    FakeInfo class
    """

    def __init__(self):
        self.fake = Faker()

    def fake_info(self, resource_type, is_solved):
        """
        Fake agent info
        """

        service_level, acr, asa, fcr, adherence = 0, 0, 0, 0, 0
        service_level_color, acr_color, asa_color, fcr_color, adherence_color = (
            "yellow",
            "red",
            "red",
            "red",
            "yellow",
        )

        if is_solved:
            service_level = random.randint(80, 100)
            service_level_color = "green"
            acr = random.randint(10, 20)
            acr_color = "green"
            asa = f"{random.randint(0, 2)}:{random.randint(0, 59)} min"
            asa_color = "green"
            fcr = random.randint(70, 80)
            fcr_color = "green"
            adherence = random.randint(60, 80)
        else:
            service_level = random.randint(20, 60)
            if service_level < 35:
                service_level_color = "red"
            acr = random.randint(40, 70)
            asa = f"{random.randint(7, 9)}:{random.randint(0, 59)} min"
            fcr = random.randint(5, 20)
            adherence = random.randint(10, 50)

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
                            "content": f"{service_level}",
                            "color": f"{service_level_color}",
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
                            "content": f"{service_level}",
                            "color": f"{service_level_color}",
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
        elif resource_type == "agent":
            return [
                {
                    "title": "Information",
                    "elements": [
                        {
                            "title": "Name",
                            "content": f"{self.fake.name()}",
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
                            "title": "ARN",
                            "content": f"agent:{random.randint(1000, 9999)}",
                            "color": "black",
                        },
                        {
                            "title": "Duration",
                            "content": f"{random.randint(7, 9)}:{random.randint(0, 59)} min",
                            "color": "red",
                        },
                        {
                            "title": "Emotion",
                            "content": "Negative",
                            "color": "red",
                        },
                    ],
                },
                {
                    "title": "Metrics",
                    "elements": [
                        {
                            "title": "Service Level",
                            "content": f"{service_level}",
                            "color": f"{service_level_color}",
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
        else:
            raise ValueError("Invalid type")
