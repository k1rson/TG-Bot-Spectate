import os, json, httpx

from config import GITHUB_TOKEN

from database.models import session, CheckerLists

async def initialize_checker_lists(user_data: dict): 
    checker_lists = session.query(CheckerLists).filter_by(user_id=user_data['user_id']).first()

    if not checker_lists: 
        data = CheckerLists(
            checker_list_github = None, 
            checker_list_twitch = None,
            checker_list_vk = None, 
            checker_list_discord = None, 
            checker_list_telegram = None, 
            user_id = user_data['user_id']
        )

        try: 
            session.add(data)
            session.commit()

            return None
        except: 
            return None
        
    return checker_lists
    
async def get_checker_list(user_data: dict) -> bool: 
    checker_lists = await initialize_checker_lists(user_data)

    if not checker_lists or not checker_lists.checker_list_github: 
        return False
    
    # parsind checker_list
    
    return checker_lists.checker_list_github
    
async def add_user_to_checker_list(username_github: str, user_data: dict) -> bool: 
    checker_lists = await initialize_checker_lists(user_data)

    if not checker_lists: 
        return False
    
    if not checker_lists.checker_list_github: 
        checker_lists.checker_list_github = [username_github]
        session.commit()

        return True
    
    checker_lists.checker_list_github = [*checker_lists.checker_list_github, username_github]
    session.commit()
    return True


async def delete_user_from_checker_list(username_github: str, user_data: dict) -> bool: 
    checker_lists = await initialize_checker_lists(user_data)

    if not checker_lists: 
        return False
    
    if not checker_lists.checker_list_github: 
        return False
    
    try: 
        checker_lists.checker_list_github = [*checker_lists.checker_list_github]
        checker_lists.checker_list_github.remove(username_github)
        session.commit()

        return True
    except: 
        return False

async def get_detail_info_about_user(username_github: str, user_data: dict) -> str:
    pass