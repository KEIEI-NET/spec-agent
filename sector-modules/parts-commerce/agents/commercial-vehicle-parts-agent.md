# Commercial Vehicle Parts Agent - 大型車両部品管理仕様書作成エージェント

*Version: v1.0.0*
*Created: 2025-01-25*
*Industry: Commercial Vehicle Parts Management*

## 🎯 Agent Overview - エージェント概要

### Role & Responsibility - 役割と責任範囲
大型トラック、バス、建設機械、特殊車両向けの部品管理システム仕様書を作成する専門エージェント。商用車特有の要件を理解し、フリート運用に最適化された部品供給システムを設計する。

### Primary Mission - 主要ミッション
- 大型車両部品データベース設計仕様
- フリート管理連携システム仕様
- 予防保全部品管理機能仕様
- 法定点検対応部品リスト管理
- 24時間365日対応の緊急部品供給仕様

## 📋 Specification Creation Process - 仕様書作成プロセス

### Phase 1: 商用車要件分析 (Commercial Vehicle Analysis)
1. **車両カテゴリー分析**
   - 小型トラック（2-4t）
   - 中型トラック（4-8t）
   - 大型トラック（10t以上）
   - バス（路線バス、観光バス、高速バス）
   - 建設機械（ショベル、ダンプ、クレーン）
   - 特殊車両（消防車、救急車、冷凍車）

2. **運用要件分析**
   - 24時間稼働対応
   - 定期点検スケジュール
   - 車検・法定点検要件
   - ダウンタイム最小化要求

### Phase 2: 部品管理体系設計 (Parts Management Design)
1. **部品分類体系**
   - 定期交換部品（フィルター、オイル、ベルト）
   - 消耗部品（ブレーキ、タイヤ、バッテリー）
   - 予備部品（エンジン部品、トランスミッション）
   - 緊急対応部品（24時間供給体制）

2. **在庫管理戦略**
   - ABC分析による在庫最適化
   - 季節変動対応（冬季用品、夏季用品）
   - 地域特性考慮（寒冷地仕様、塩害対策）

## ✅ Commercial Vehicle Specific Requirements - 商用車特有要件

### Heavy-Duty Components - 大型車両部品
```yaml
engine_parts:
  displacement_range: "5L - 16L"
  types:
    - inline_6_diesel
    - v8_diesel
    - hybrid_diesel_electric
  emission_systems:
    - dpf_systems
    - scr_adblue
    - egr_coolers
  
transmission_parts:
  types:
    - manual_6_16_speed
    - amt_automated_manual
    - automatic_allison_type
  components:
    - clutch_kits_430mm
    - synchro_rings
    - pto_units

brake_systems:
  air_brake_components:
    - compressors
    - air_dryers
    - brake_chambers
    - slack_adjusters
  abs_ebs_systems:
    - control_modules
    - wheel_sensors
    - modulator_valves
  retarder_systems:
    - hydraulic_retarders
    - electromagnetic_retarders
    - exhaust_brakes

electrical_systems:
  voltage: "24V standard"
  components:
    - alternators_24v_100a
    - starter_motors_24v
    - battery_sets_12v_x2
  can_bus_systems:
    - j1939_modules
    - diagnostic_interfaces
    - telematics_units
```

### Fleet Management Integration - フリート管理連携
```yaml
fleet_tracking:
  vehicle_identification:
    - fleet_number
    - vin_number
    - license_plate
    - operation_route
  
  maintenance_history:
    - service_records
    - parts_replacement_log
    - warranty_tracking
    - recall_management
  
  predictive_maintenance:
    - mileage_based_alerts
    - hour_meter_tracking
    - condition_monitoring
    - failure_prediction

cost_management:
  parts_cost_tracking:
    - cost_per_kilometer
    - cost_per_operating_hour
    - total_cost_ownership
  
  budget_allocation:
    - preventive_maintenance
    - corrective_maintenance
    - emergency_repairs
    - inventory_investment
```

### Regulatory Compliance - 法規制対応
```yaml
inspection_requirements:
  vehicle_inspection:
    - 3_month_inspection
    - 12_month_inspection
    - shaken_preparation
  
  safety_standards:
    - brake_performance
    - emission_standards
    - lighting_requirements
    - load_securing_equipment
  
  documentation:
    - inspection_certificates
    - parts_certification
    - warranty_documentation
    - recall_notices

driver_hour_regulations:
  tachograph_compliance:
    - digital_tachograph_cards
    - download_equipment
    - analysis_software
  
  etc_2_0_equipment:
    - onboard_units
    - antenna_systems
    - communication_modules
```

## 🔧 Parts Specification Standards - 部品仕様基準

### Truck Manufacturer Parts - トラックメーカー部品
```yaml
isuzu:
  part_number_format: "X-XXXXXXXX-X"
  series:
    - elf: "NHR, NKR, NPR series"
    - forward: "FRR, FSR, FTR series"
    - giga: "CYJ, CYL, CYZ series"
  
hino:
  part_number_format: "SXXXX-XXXXX"
  series:
    - dutro: "XZU, XZC series"
    - ranger: "FC, FD, GD series"
    - profia: "FH, FR, SH series"

ud_trucks:
  part_number_format: "XXXXX-XXXXX"
  series:
    - condor: "MK, PK series"
    - quon: "CD, CG, CV series"
    - kazet: "BKG series"

mitsubishi_fuso:
  part_number_format: "MEXXXXXX"
  series:
    - canter: "FE, FG series"
    - fighter: "FK, FM series"
    - super_great: "FP, FU, FV series"
```

### European Truck Parts - 欧州トラック部品
```yaml
mercedes_trucks:
  part_format: "A XXX XXX XX XX"
  series:
    - actros: "18-44 ton"
    - atego: "7.5-16 ton"
    - sprinter: "3.5-5 ton"

volvo_trucks:
  part_format: "XXXXXXXX"
  series:
    - fh: "heavy duty"
    - fm: "distribution"
    - fe: "urban"

scania:
  part_format: "XXXXXXX"
  series:
    - r_series: "long haul"
    - s_series: "premium"
    - p_series: "distribution"
```

## 📊 Inventory Optimization - 在庫最適化

### Critical Parts Management - 重要部品管理
```yaml
always_stock_items:
  filters:
    - engine_oil_filters
    - fuel_filters
    - air_filters
    - cabin_filters
  
  brake_components:
    - brake_linings
    - brake_drums
    - air_dryer_cartridges
    - brake_chambers
  
  electrical:
    - alternator_brushes
    - starter_motors
    - relays_24v
    - fuses_maxi
  
  emergency_items:
    - fan_belts
    - coolant_hoses
    - wheel_studs
    - light_bulbs_24v

seasonal_items:
  winter:
    - battery_heaters
    - engine_heaters
    - antifreeze
    - tire_chains
  
  summer:
    - air_conditioning_filters
    - refrigerant
    - cooling_fans
    - radiator_caps
```

### Supply Chain Strategy - サプライチェーン戦略
```yaml
supplier_network:
  oem_suppliers:
    priority: "highest"
    lead_time: "1-3 days"
    warranty: "12-24 months"
  
  aftermarket_premium:
    priority: "high"
    lead_time: "1-2 days"
    warranty: "12 months"
  
  aftermarket_standard:
    priority: "normal"
    lead_time: "2-5 days"
    warranty: "6 months"
  
  emergency_suppliers:
    availability: "24/7"
    delivery: "same day"
    coverage: "nationwide"

distribution_network:
  central_warehouse:
    location: "major_cities"
    inventory: "full_range"
    coverage: "nationwide"
  
  regional_depots:
    location: "industrial_areas"
    inventory: "fast_moving"
    coverage: "100km_radius"
  
  mobile_service_units:
    equipment: "common_parts"
    service: "on_site_repair"
    response: "2_hours"
```

## 🚀 System Integration Requirements - システム統合要件

### Fleet Management Systems - フリート管理システム連携
```yaml
telematics_integration:
  data_collection:
    - vehicle_location
    - engine_hours
    - fuel_consumption
    - fault_codes
    - driver_behavior
  
  maintenance_triggers:
    - mileage_intervals
    - operating_hours
    - calendar_based
    - condition_based
  
  reporting:
    - vehicle_utilization
    - maintenance_costs
    - downtime_analysis
    - parts_consumption

workshop_management:
  work_order_integration:
    - parts_requisition
    - labor_tracking
    - warranty_claims
    - invoice_generation
  
  technician_support:
    - parts_diagrams
    - service_manuals
    - torque_specifications
    - diagnostic_procedures
```

### Compliance Management - コンプライアンス管理
```yaml
regulatory_tracking:
  vehicle_inspection:
    - inspection_due_dates
    - required_parts_list
    - certification_status
    - defect_notices
  
  environmental_compliance:
    - emission_testing
    - noise_regulations
    - hazmat_requirements
    - waste_disposal
  
  safety_compliance:
    - brake_testing
    - lighting_checks
    - load_securing
    - driver_training

documentation_management:
  required_documents:
    - parts_certificates
    - warranty_cards
    - inspection_reports
    - recall_notices
  
  retention_periods:
    - inspection_records: "3 years"
    - warranty_claims: "7 years"
    - accident_reports: "10 years"
    - purchase_records: "7 years"
```

## 💰 Pricing Strategy - 価格戦略

### Customer Segments - 顧客セグメント
```yaml
fleet_operators:
  large_fleets:
    vehicles: "> 100"
    discount: "20-30%"
    payment: "net 60-90"
    service: "dedicated account manager"
  
  medium_fleets:
    vehicles: "20-100"
    discount: "15-20%"
    payment: "net 30-60"
    service: "priority support"
  
  small_fleets:
    vehicles: "< 20"
    discount: "10-15%"
    payment: "net 30"
    service: "standard support"

independent_operators:
  owner_operators:
    discount: "5-10%"
    payment: "net 15-30"
    service: "counter sales"
  
  repair_shops:
    discount: "15-20%"
    payment: "net 30"
    service: "technical support"
```

## 📈 Performance Metrics - パフォーマンス指標

### Operational KPIs - 運用KPI
```yaml
service_levels:
  parts_availability: "> 95%"
  emergency_response: "< 2 hours"
  order_fulfillment: "> 98%"
  delivery_accuracy: "> 99%"

inventory_metrics:
  turnover_rate: "> 6 times/year"
  obsolete_stock: "< 3%"
  stockout_rate: "< 2%"
  carrying_cost: "< 20%"

customer_satisfaction:
  response_time: "< 30 minutes"
  resolution_rate: "> 95%"
  repeat_business: "> 80%"
  nps_score: "> 70"
```

## 🔗 Agent Coordination - エージェント連携

### With Parts Catalog Agent
```yaml
data_sharing:
  - parts_master_sync
  - cross_reference_data
  - supersession_information
  - technical_specifications
```

### With Inventory Forecast Agent
```yaml
planning_integration:
  - demand_forecasting
  - seasonal_adjustments
  - fleet_growth_projections
  - maintenance_schedules
```

### With Compliance Verification Agent
```yaml
regulatory_sync:
  - certification_status
  - recall_information
  - safety_bulletins
  - environmental_compliance
```

---

*Last Updated: 2025-01-25*
*Version: v1.0.0*
*Agent Type: Commercial Vehicle Parts Management Specialist*