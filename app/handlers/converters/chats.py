from dtos.messages import ChatListItemDTO


def convert_chats_dtos_to_message(chats: list[ChatListItemDTO]) -> str:
    return '\n\n'.join(
        (
            'List of all available chats',
            '\n\n'.join(
                (f'chatOID: `{chat.oid}`\. Problem: {chat.title}' for chat in chats)
            )
        )
    )
