from modules.models.auth.account import Account
from modules.models.launch.game_window_config import GameWindowConfig
from modules.models.launch.jvm_config import JvmConfig
from modules.models.launch.sever_config import SeverConfig


class LaunchConfig():
    def __init__(self, account: Account, jvm_config: JvmConfig, game_window_config: GameWindowConfig, sever_config: SeverConfig = None, is_enable_independency_core: bool = True):
        self.account = account
        self.jvm_config = jvm_config
        self.game_window_config = game_window_config
        self.server_config = sever_config
        self.natives_folder: str = None
        self.working_folder: str
        self.launch_name: str = "minecraft-launch-p"
        self.is_server: bool = True
        self.is_enable_independency_core: bool = is_enable_independency_core