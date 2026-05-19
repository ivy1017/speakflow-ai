import Recorder from "./components/Recorder";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-6">
      <h1 className="text-4xl font-bold">SpeakFlow AI</h1>

      <Recorder />
    </main>
  );
}
