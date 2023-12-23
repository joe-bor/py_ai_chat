import { useState } from "react";
import axios from "axios";

type Props = {
  setMessages: any;
};

function Title({ setMessages }: Props) {
  const [isResetting, setIsResetting] = useState(false);

  // Reset the convo
  const resetConversation = async () => {
    setIsResetting(true);

    axios
      .get("http://localhost:8000/reset")
      .then((res) => {
        if (res.status === 200) {
          setMessages([]);
        } else {
          console.error(
            "There was an error with API request to /reset endpoint."
          );
        }
      })
      .catch((err) => {
        console.error(err.messages);
      });

    setIsResetting(false);
  };

  return (
    <div>
      <button className="bg-indigo-500" onClick={resetConversation}>
        RESET
      </button>
    </div>
  );
}

export default Title;
