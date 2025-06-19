import unittest
from unittest.mock import patch, MagicMock
import os
from yt_dlp.options import parseOpts

class TestLoadFromConfigDirs(unittest.TestCase):

    def test_invalid_path_raises_assertion_error(self):
        """
        Caso de Teste CT1: Testa um caminho inválido.
        Cobre a linha 1 da tabela verdade (C1=F, C2=F).
        """
        with patch('yt_dlp.options.get_executable_path', return_value='/some/invalid/path'):
            with patch('yt_dlp.options.get_user_config_dirs', return_value=['/some/invalid/path']):
                with self.assertRaises(SystemExit): 
                    parseOpts(['--help'])  

    @patch('os.path.expanduser')
    @patch('yt_dlp.options.get_user_config_dirs')
    def test_home_dot_path_succeeds(self, mock_get_user_dirs, mock_expanduser):
        """
        Caso de Teste CT2: Testa o caminho no diretório home do usuário.
        Cobre a linha 2 da tabela verdade (C1=F, C2=V).
        """
        mock_expanduser.return_value = '/home/user'
        mock_get_user_dirs.return_value = ['/home/user/.yt-dlp']
        
        try:
            parseOpts(['--version']) 
        except SystemExit:
            pass

    @patch('yt_dlp.options.get_system_config_dirs')
    def test_standard_config_path_succeeds(self, mock_get_system_dirs):
        """
        Caso de Teste CT3: Testa um caminho de configuração padrão.
        Cobre a linha 3 da tabela verdade (C1=V, C2=F).()=>
        """
        mock_get_system_dirs.return_value = ['/etc/yt-dlp']
        
        try:
            parseOpts(['--version']) 
        except SystemExit: 
            pass  
