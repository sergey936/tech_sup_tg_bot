from dtos.messages import ChatListItemDTO


def convert_chats_dtos_to_message(chats: list[ChatListItemDTO]) -> str:
    return '\n'.join(
        (
            'List of all avaible chats',
            '\n'.join(
                (f'chatOID: `{chat.oid}`\. Problem: {chat.title}' for chat in chats)
            )
        )
    )
