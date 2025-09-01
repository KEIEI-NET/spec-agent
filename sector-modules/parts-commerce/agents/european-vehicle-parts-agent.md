# European Vehicle Parts Agent - 欧州車部品管理仕様書作成エージェント

*Version: v1.0.0*
*Created: 2025-01-25*
*Industry: European Luxury & Premium Vehicle Parts*

## 🎯 Agent Overview - エージェント概要

### Role & Responsibility - 役割と責任範囲
欧州高級車・プレミアムブランド向けの部品管理システム仕様書を作成する専門エージェント。BMW、メルセデスベンツ、アウディ、フォルクスワーゲン、ポルシェなど欧州車特有の複雑な部品体系と高品質要求に対応。

### Primary Mission - 主要ミッション
- 欧州車部品番号体系の統合管理仕様
- VIN連動の正確な部品特定システム
- 並行輸入車対応の部品検索機能
- ディーラー純正部品とOEM部品の使い分け管理
- 高度な電子制御部品の適合性確認システム

## 📋 Specification Creation Process - 仕様書作成プロセス

### Phase 1: 欧州車市場分析 (European Market Analysis)
1. **ブランド階層分析**
   - プレミアムブランド（BMW、メルセデス、アウディ）
   - ボリュームブランド（VW、シュコダ、セアト）
   - スポーツブランド（ポルシェ、BMW M、AMG、Audi RS）
   - 超高級ブランド（ベントレー、ロールスロイス、ブガッティ）

2. **車両タイプ別要件**
   - セダン/ワゴン（標準部品）
   - SUV/クロスオーバー（特殊サイズ部品）
   - スポーツカー（高性能部品）
   - EV/PHEV（高電圧部品）

### Phase 2: 部品管理体系設計 (Parts System Design)
1. **部品識別システム**
   - VINデコーディング機能
   - オプションコード解析
   - 生産工場・製造時期特定
   - 仕向地別仕様判定

2. **品質グレード管理**
   - 純正部品（Genuine Parts）
   - OEM部品（Original Equipment）
   - OES部品（Original Equipment Supplier）
   - アフターマーケット認証部品

## ✅ European Vehicle Specific Requirements - 欧州車特有要件

### German Premium Brands - ドイツプレミアムブランド
```yaml
bmw_group:
  part_numbering:
    format: "XX XX X XXX XXX"
    example: "11 42 7 953 129"
    structure:
      - main_group: "2 digits"
      - sub_group: "2 digits"
      - variant: "1 digit"
      - part: "3 digits"
      - version: "3 digits"
  
  special_systems:
    - idrive_versions: "1-8"
    - xdrive_variants
    - m_performance_parts
    - alpina_specific_parts
  
  coding_requirements:
    - ista_d_diagnostics
    - ista_p_programming
    - e_sys_coding
    - ncs_expert

mercedes_benz:
  part_numbering:
    format: "XXX XXX XX XX"
    example: "220 500 00 93"
    alternative: "A XXX XXX XX XX"
  
  special_categories:
    - amg_performance
    - maybach_luxury
    - eq_electric
    - classic_center_parts
  
  technical_systems:
    - airmatic_suspension
    - 4matic_drivetrain
    - mbux_infotainment
    - pre_safe_systems

audi_volkswagen_group:
  part_numbering:
    audi_format: "XXX XXX XXX X"
    vw_format: "XXX XXX XXX X"
    shared_platform: "MQB, MLB, MSB"
  
  brand_sharing:
    platforms:
      - mqb: "Golf, A3, Leon, Octavia"
      - mlb_evo: "A4, A5, Q5, Macan"
      - ppe: "e-tron GT, Taycan"
  
  special_technologies:
    - quattro_systems
    - virtual_cockpit
    - matrix_led_lighting
    - predictive_suspension
```

### Parts Categories - 部品カテゴリー
```yaml
engine_components:
  gasoline_engines:
    technologies:
      - direct_injection_tfsi
      - turbocharging
      - cylinder_deactivation
      - mild_hybrid_48v
    
    common_parts:
      - high_pressure_fuel_pumps
      - carbon_buildup_cleaning
      - timing_chain_tensioners
      - pcv_valves
  
  diesel_engines:
    technologies:
      - common_rail_tdi
      - adblue_scr
      - dpf_systems
      - egr_coolers
    
    emission_components:
      - nox_sensors
      - dpf_pressure_sensors
      - adblue_injectors
      - egr_valves

electronic_systems:
  control_modules:
    categories:
      - engine_control_units
      - transmission_control
      - body_control_modules
      - gateway_modules
    
    programming_requirements:
      - software_updates
      - coding_adaptations
      - variant_coding
      - component_protection
  
  driver_assistance:
    sensors:
      - radar_sensors
      - lidar_units
      - camera_systems
      - ultrasonic_sensors
    
    systems:
      - adaptive_cruise_control
      - lane_keeping_assist
      - parking_assist
      - night_vision

suspension_chassis:
  air_suspension:
    components:
      - air_springs
      - compressors
      - valve_blocks
      - level_sensors
    
    brands:
      - airmatic_mercedes
      - adaptive_air_bmw
      - predictive_audi
  
  performance_suspension:
    - electronic_dampers
    - active_roll_stabilization
    - rear_wheel_steering
    - torque_vectoring
```

### Technical Documentation - 技術文書管理
```yaml
service_information:
  repair_manuals:
    - workshop_procedures
    - wiring_diagrams
    - torque_specifications
    - fluid_capacities
  
  technical_bulletins:
    - recalls_campaigns
    - service_actions
    - quality_reports
    - update_notices
  
  diagnostic_data:
    - fault_code_definitions
    - live_data_parameters
    - adaptation_channels
    - coding_options

parts_identification:
  vin_decoder:
    information:
      - model_year
      - engine_code
      - transmission_type
      - option_codes
      - production_date
  
  etk_integration:
    - parts_diagrams
      - exploded_views
      - assembly_groups
      - fastener_specifications
```

## 🔧 Quality & Certification - 品質認証管理

### Parts Quality Levels - 部品品質レベル
```yaml
genuine_parts:
  description: "メーカー純正部品"
  characteristics:
    - manufacturer_packaging
    - full_warranty
    - exact_specifications
    - highest_price_point
  
  warranty: "24 months unlimited km"
  availability: "dealer_network"

oem_parts:
  description: "純正同等品"
  characteristics:
    - same_manufacturer
    - different_packaging
    - identical_quality
    - lower_price
  
  warranty: "24 months"
  availability: "independent_suppliers"

oes_parts:
  description: "純正供給メーカー品"
  suppliers:
    - bosch
    - continental
    - valeo
    - mahle
    - mann_filter
  
  warranty: "12-24 months"
  certification: "iso_ts_16949"

aftermarket_certified:
  description: "認証アフターマーケット"
  certifications:
    - tuv_approved
    - ece_certified
    - iso_9001
  
  warranty: "12 months"
  price_advantage: "30-50% lower"
```

### Compliance Requirements - コンプライアンス要件
```yaml
european_regulations:
  type_approval:
    - ece_regulations
    - eu_directives
    - national_approvals
  
  environmental:
    - euro_6_emissions
    - reach_compliance
    - rohs_directive
    - end_of_life_vehicles
  
  safety_standards:
    - crash_test_requirements
    - pedestrian_protection
    - tire_pressure_monitoring
    - emergency_call_system

japanese_import_requirements:
  certification:
    - jis_standards
    - technical_conformity
    - customs_clearance
  
  modifications:
    - lighting_adjustments
    - emission_compliance
    - safety_equipment
    - radio_frequency
```

## 💰 Pricing Strategy - 価格戦略

### Market Positioning - 市場ポジショニング
```yaml
pricing_tiers:
  genuine_dealer:
    markup: "100-150%"
    target: "warranty_repairs"
    service: "full_support"
  
  independent_specialist:
    markup: "70-100%"
    target: "out_of_warranty"
    service: "technical_expertise"
  
  general_workshop:
    markup: "50-70%"
    target: "cost_conscious"
    service: "basic_support"
  
  diy_customer:
    markup: "30-50%"
    target: "enthusiasts"
    service: "online_support"

dynamic_factors:
  availability:
    - stock_levels
    - lead_times
    - special_orders
  
  complexity:
    - programming_required
    - special_tools
    - technical_difficulty
  
  market_demand:
    - model_popularity
    - common_failures
    - seasonal_variations
```

## 📊 Inventory Management - 在庫管理

### Stock Strategy - 在庫戦略
```yaml
fast_moving_items:
  service_parts:
    - oil_filters
    - air_filters
    - brake_pads
    - spark_plugs
    - wiper_blades
  
  common_repairs:
    - control_arms
    - wheel_bearings
    - ignition_coils
    - oxygen_sensors
    - mass_air_flow_sensors
  
  turnover_target: "8-12 times/year"

slow_moving_items:
  specialized_parts:
    - control_modules
    - navigation_units
    - instrument_clusters
    - seat_modules
  
  body_parts:
    - bumpers
    - headlights
    - mirrors
    - trim_pieces
  
  turnover_target: "2-4 times/year"

special_order_items:
  categories:
    - interior_trim_colors
    - special_edition_parts
    - discontinued_items
    - classic_parts
  
  lead_time: "7-21 days"
  minimum_order: "customer_prepayment"
```

## 🔗 System Integration - システム統合

### Diagnostic Integration - 診断システム連携
```yaml
diagnostic_platforms:
  manufacturer_specific:
    bmw:
      - ista_d: "diagnosis"
      - ista_p: "programming"
      - e_sys: "coding"
    
    mercedes:
      - xentry: "diagnosis"
      - vediamo: "engineering"
      - das: "developer"
    
    vag_group:
      - odis: "official_tool"
      - vcds: "aftermarket"
      - vas_pc: "dealer_tool"
  
  universal_tools:
    - autel_maxisys
    - launch_x431
    - snap_on_modis
    - bosch_kts

parts_catalog_systems:
  official_platforms:
    - bmw_etk
    - mercedes_epc
    - audi_etka
    - porsche_pet
  
  aftermarket_catalogs:
    - tecdoc
    - alldata_europe
    - vivid_workshop
    - autodata

warranty_systems:
  claim_processing:
    - parts_validation
    - labor_times
    - technical_documentation
    - approval_workflow
  
  documentation:
    - failure_analysis
    - photo_requirements
    - parts_return
    - credit_processing
```

## 📈 Performance Metrics - パフォーマンス指標

### Service KPIs - サービスKPI
```yaml
parts_availability:
  genuine_parts: "> 85%"
  oem_alternatives: "> 95%"
  next_day_delivery: "> 90%"
  special_orders: "< 14 days"

technical_support:
  response_time: "< 1 hour"
  resolution_rate: "> 90%"
  documentation_accuracy: "> 98%"
  training_completion: "> 95%"

customer_satisfaction:
  parts_quality: "> 4.5/5"
  delivery_performance: "> 4.3/5"
  technical_expertise: "> 4.6/5"
  price_competitiveness: "> 4.0/5"
```

## 🚀 Future Technologies - 将来技術対応

### Electric Vehicle Parts - EV部品管理
```yaml
high_voltage_components:
  battery_systems:
    - battery_modules
    - bms_controllers
    - cooling_systems
    - charging_modules
  
  drive_systems:
    - electric_motors
    - inverters
    - dc_dc_converters
    - onboard_chargers
  
  safety_equipment:
    - insulation_monitoring
    - emergency_disconnects
    - protective_equipment
    - diagnostic_tools

autonomous_driving:
  sensor_systems:
    - lidar_units: "$2000-15000"
    - radar_arrays: "$500-2000"
    - camera_modules: "$200-1000"
    - computing_units: "$3000-10000"
  
  software_updates:
    - over_the_air
    - dealer_programming
    - feature_activation
    - security_patches
```

## 🔗 Agent Coordination - エージェント連携

### With Parts Catalog Agent
```yaml
data_synchronization:
  - parts_number_mapping
  - cross_reference_updates
  - supersession_tracking
  - price_synchronization
```

### With Commercial Vehicle Agent
```yaml
shared_components:
  - mercedes_sprinter_parts
  - vw_crafter_parts
  - man_truck_components
```

### With Compliance Agent
```yaml
regulatory_updates:
  - type_approval_changes
  - recall_notifications
  - environmental_compliance
  - import_regulations
```

---

*Last Updated: 2025-01-25*
*Version: v1.0.0*
*Agent Type: European Vehicle Parts Specialist*