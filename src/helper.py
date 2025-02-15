
def get_user_stories(response):
    response_object = ''
    for each_category in response:
        response_object += f"Category: {each_category['category']}\n\n"
        for each_story in each_category['stories']:
            response_object += f"User Story: {each_story['description']}\n"
            if 'acceptance_criteria' in each_story:
                response_object += f"Acceptance Criteria: {each_story['acceptance_criteria']}\n"
        response_object += f"-----------------------------------\n"
    return response_object

