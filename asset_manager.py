# asset_manager.py
"""Asset loading and management"""

import pygame
from constants import CARD_DIMENSIONS, ASSETS

class AssetManager:
    def __init__(self):
        self.assets = {}
        self.load_assets()
    
    def load_assets(self):
        """Load and scale all game assets"""
        for name, path in ASSETS.items():
            try:
                asset = pygame.image.load(path)
                scaled_asset = pygame.transform.scale(asset, CARD_DIMENSIONS)
                self.assets[name] = scaled_asset
                print(f"Loaded {name} asset: {asset.get_width()}x{asset.get_height()}")
            except pygame.error as e:
                print(f"Error loading asset {name}: {e}")
                # Create a placeholder surface if asset fails to load
                self.assets[name] = self.create_placeholder()
    
    def create_placeholder(self):
        """Create a placeholder surface for missing assets"""
        surface = pygame.Surface(CARD_DIMENSIONS)
        surface.fill((100, 100, 100))  # Gray placeholder
        return surface
    
    def get_asset(self, name):
        """Get an asset by name"""
        return self.assets.get(name, self.create_placeholder())