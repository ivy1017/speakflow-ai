import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "SpeakFlow AI",
  description: "AI 语音工具",
};

// 默认导出一个 React 函数组件
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
