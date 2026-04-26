#!/usr/bin/env python3
"""CI 脚本：基于 VERSIONS.json 和 PR 目标分支，执行版本合规检查。"""

import json
import os
import sys

def load_versions(versions_path='governance/VERSIONS.json'):
    with open(versions_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    # 从 GitHub Actions 环境变量获取 PR 目标分支
    target_branch = os.environ.get('GITHUB_BASE_REF', 'main')

    versions_data = load_versions()
    maintenance_versions = [v['version'] for v in versions_data['sinoshop_versions']['maintenance']]
    eol_versions = [v['version'] for v in versions_data['sinoshop_versions']['eol']]

    # 提取分支名中的主版本号（假设分支命名如: 2.x, 3.x, 1.x 等）
    target_version = target_branch

    if target_version in eol_versions:
        print(f"❌ 错误：分支 {target_branch} 对应的版本 {target_version} 已终止生命周期 (EOL)。")
        print("   除非是紧急安全补丁，否则禁止合并。请使用 [SECURITY] 标签注明。")
        sys.exit(1)  # 构建失败
    elif target_version in maintenance_versions:
        print(f"⚠️ 警告：分支 {target_branch} 处于维护模式 (Maintenance)。")
        print("   该分支仅接受安全修复。请确保 PR 未包含新功能或 API 变更。")
    else:
        print(f"✅ 分支 {target_branch} (版本 {target_version}) 处于活跃状态 (Active)，检查通过。")

    sys.exit(0)

if __name__ == '__main__':
    main()
