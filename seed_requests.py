from data import requests_data


def seed_requests():

    dummy = [

        {
            "request_no": "REQ001",
            "owner": "Karan",
            "request_for": "Library",
            "subject": "Need new React book",
            "comments": "For learning advanced patterns",

            "open_date": "2026-04-17",
            "close_date": "",
            "actual_closed_date": "",

            "user_status": "Open",
            "request_status": "Pending",

            "report_to": "Admin",

            "response_status": "Pending",

            "active": True
        },


        {
            "request_no": "REQ002",
            "owner": "Karan",
            "request_for": "IT",
            "subject": "VS Code extension install",
            "comments": "Need Prettier & ESLint",

            "open_date": "2026-04-18",
            "close_date": "",
            "actual_closed_date": "",

            "user_status": "Open",
            "request_status": "Pending",

            "report_to": "IT Team",

            "response_status": "Pending",

            "active": True
        },


        {
            "request_no": "REQ003",
            "owner": "Karan",
            "request_for": "Stationary",
            "subject": "Notebook & pen",
            "comments": "",

            "open_date": "2026-04-10",
            "close_date": "2026-04-12",
            "actual_closed_date": "2026-04-12",

            "user_status": "Closed",
            "request_status": "Approved",

            "report_to": "Admin",

            "response_status": "Approved",

            "active": True
        }

    ]


    requests_data.clear()

    requests_data.extend(dummy)

    print(f"Dummy requests inserted: {len(dummy)}")


if __name__ == "__main__":

    seed_requests()