# Architecture

## Overview
Simple 3-layer architecture:
- **Models**: Data classes with load/save methods
- **Utils**: Shared helper functions
- **Config**: Environment-based configuration

## Data Flow
1. CSV/JSON files → Model classes → Application logic
2. Orders reference Users and Products by ID
