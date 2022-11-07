import DiscordRPC

def run_rpc():
    rpc = DiscordRPC.RPC.Set_ID(app_id=1039211098685059153)
    button = DiscordRPC.button(
        button_one_label="Download!",
        button_one_url="https://github.com/ahhyoushh/console-game",
        button_two_label="My github!",
        button_two_url="https://github.com/ahhyoushh"
    )
    rpc.set_activity(
        state="Active!",
        details="playing console game by fr._.#2525",
        large_image="large",
        large_text="Console game",
        buttons=button,
        timestamp=rpc.timestamp()
    )
    rpc.run()
