from collections import deque


class Solution:
    def bfs(root):
        visited = []
        # root가 None이면 0을 반환
        if root is None:
            return 0

        # 큐 생성
        que = deque()
        # 큐에 root 값 넣어주기
        que.append(root)

        # 큐가 있는 동안 while문 실행
        while que:
            # root에 접근 que에서 pop 하고 튀어나옴
            cur_node = que.popleft()
            # 방명록에 root A의 값 추가
            visited.append(cur_node.value)

            #      A
            #   B     C
            # D  E   F  G
            if cur_node.left:
                # A 노드의 레프트 B 방문 예정이므로 que에 push
                que.append(cur_node.left)
            if cur_node.right:
                # A 노드의 라이트 C 방문 예정이므로 que에 push
                que.append(cur_node.right)

        return visited

