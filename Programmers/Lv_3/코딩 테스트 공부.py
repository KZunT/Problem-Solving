def solution(alp, cop, problems):
    need_alp_req, need_cop_req = 0,0  # 모든 문제를 풀기위한 알고력과 코테력 계산

    for problem in problems:
        need_alp_req = max(need_alp_req, problem[0])
        need_cop_req = max(need_cop_req, problem[1])

    dp = [[float('inf')] * (need_cop_req + 1) for _ in range(need_alp_req + 1)] # 걸리는 최소시간을 계산하기 위한 dp 테이블 무한 값으로 초기화

    # 목표 알고력과 목표 코딩력을 넘는 경우 방지, 넘는 경우 인덱스 에러 유발 가능
    alp = min(alp, need_alp_req)
    cop = min(cop, need_cop_req)

    dp[alp][cop] = 0  # 현재 상태, 걸리는 시간

    # 현재 능력부터 목표 능력까지 반복

    for i in range(alp, need_alp_req + 1):
        for j in range(cop, need_cop_req + 1):
            # 현재 능력이 목표보다 낮을 때 시간을 투자하여 능력을 늘리기
            if i < need_alp_req:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < need_cop_req:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            # 현재 능력이 목표보다 낮을 때 풀 수 있는 문제를 풀어서 능력을 늘리는 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 풀 수 있는 문제 선발
                if i >= alp_req and j >= cop_req:
                    # 문제를 풀었을 경우 오르는 능력이 목표 능력을 넘는 경우 방지, 넘는 경우 인덱스 에러 유발 가능
                    new_alp = min(i + alp_rwd, need_alp_req)
                    new_cop = min(j + cop_rwd, need_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)  # 최소 시간 업데이트

    return dp[need_alp_req][need_cop_req]